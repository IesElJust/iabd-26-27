"""Registre local d'experiments amb SQLite, sense servidor extern."""
from pathlib import Path
import hashlib, json, sys
import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error

def main():
    out = Path(__file__).resolve().parent / 'eixides'
    out.mkdir(exist_ok=True)
    # La base local guarda metadades; els artefactes van a una altra carpeta.
    mlflow.set_tracking_uri('sqlite:///' + str(out / 'mlflow.db'))
    experiment = 'energia-docent'
    if mlflow.get_experiment_by_name(experiment) is None:
        mlflow.create_experiment(experiment, artifact_location=(out / 'artifacts').as_uri())
    mlflow.set_experiment(experiment)
    rng = np.random.default_rng(42)
    X = rng.normal(size=(150, 2))
    y = 10 + 3 * X[:, 0] - 2 * X[:, 1] + rng.normal(0, 0.5, 150)
    (train, valid) = (X[:100], X[100:])
    (yt, yv) = (y[:100], y[100:])
    # Empremta de la representació concreta usada en este experiment.
    fingerprint = hashlib.sha256(X.tobytes() + y.tobytes()).hexdigest()
    run_ids = []
    # Comparem paràmetres mantenint dades i partició constants.
    for alpha in [0.1, 10.0]:
        model = Ridge(alpha=alpha).fit(train, yt)
        with mlflow.start_run(run_name=f'ridge-alpha-{alpha}') as run:
            mlflow.log_params({'alpha': alpha, 'seed': 42, 'train_rows': 100, 'valid_rows': 50})
            mlflow.set_tags({'data_sha256': fingerprint, 'split': '100/50 iid sintetiques', 'python': sys.version.split()[0]})
            mlflow.log_metric('mae_valid', mean_absolute_error(yv, model.predict(valid)))
            mlflow.log_text('Dades sintètiques; comparació en validació, sense test final en esta demo.', 'decisions.txt')
            mlflow.sklearn.log_model(model, name='model', input_example=train[:2])
            run_ids.append(run.info.run_id)
    # Comprovem que les execucions han acabat i es poden recuperar.
    runs = mlflow.search_runs(experiment_names=[experiment], filter_string="attributes.status = 'FINISHED'")
    assert set(run_ids).issubset(set(runs.run_id))
    print(runs[['run_id', 'params.alpha', 'metrics.mae_valid']].head().to_string(index=False))
    (out / 'execucio.json').write_text(json.dumps({'run_ids': run_ids, 'data_sha256': fingerprint}, indent=2))
    print('Tracking URI:', mlflow.get_tracking_uri())
if __name__ == '__main__':
    main()
