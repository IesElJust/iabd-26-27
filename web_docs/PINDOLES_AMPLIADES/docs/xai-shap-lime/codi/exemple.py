"""Explicacions d'un model de consum sintètic; no inferència causal."""
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.inspection import permutation_importance
from sklearn.metrics import mean_absolute_error
import shap
from lime.lime_tabular import LimeTabularExplainer

def main():
    rng = np.random.default_rng(21)
    X = pd.DataFrame({'superficie': rng.uniform(40, 180, 300), 'ocupants': rng.integers(1, 6, 300), 'soroll': rng.normal(0, 1, 300)})
    y = 20 + 0.45 * X.superficie + 8 * X.ocupants + rng.normal(0, 4, len(X))
    (train, valid, yt, yv) = train_test_split(X, y, test_size=0.25, random_state=42)
    model = RandomForestRegressor(n_estimators=60, min_samples_leaf=4, random_state=42, n_jobs=1).fit(train, yt)
    print('MAE de validació:', mean_absolute_error(yv, model.predict(valid)))
    # Importància sobre validació: no sobre les dades d’ajust.
    perm = permutation_importance(model, valid, yv, scoring='neg_mean_absolute_error', n_repeats=5, random_state=42)
    print('Importància per permutació:', dict(zip(X.columns, perm.importances_mean)))
    # La referència SHAP procedix d’entrenament i queda documentada.
    background = train.sample(60, random_state=42)
    explainer = shap.TreeExplainer(model, data=background, feature_perturbation='interventional')
    explanation = explainer(valid.iloc[:5])
    # Comprovem l’additivitat en l’escala de regressió del model.
    reconstruction = explanation.base_values + explanation.values.sum(axis=1)
    assert np.allclose(reconstruction, model.predict(valid.iloc[:5]), atol=0.0001)
    print('Predicció local:', model.predict(valid.iloc[[0]])[0])
    print('Base:', explanation.base_values[0], 'Contribucions:', explanation.values[0])

    def predict(array):
        return model.predict(pd.DataFrame(array, columns=X.columns))
    local = LimeTabularExplainer(train.to_numpy(), feature_names=list(X.columns), mode='regression', random_state=42)
    # Exigim revisar la fidelitat local abans d’interpretar els pesos.
    result = local.explain_instance(valid.iloc[0].to_numpy(), predict, num_features=3, num_samples=1000)
    print('LIME:', result.as_list(), 'Fidelitat local:', result.score)
    out = Path(__file__).resolve().parent / 'eixides'
    out.mkdir(exist_ok=True)
    pd.DataFrame(explanation.values, columns=X.columns).to_csv(out / 'shap-local.csv', index=False)
    result.save_to_file(str(out / 'lime-local.html'))
if __name__ == '__main__':
    main()
