"""Regressió sobre observacions independents sintètiques, no una sèrie temporal."""
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.dummy import DummyRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

def main():
    rng = np.random.default_rng(12)
    X = pd.DataFrame({'superficie': rng.uniform(40, 180, 480), 'aillament': rng.choice(['baix', 'alt'], 480)})
    y = 12 + 0.4 * X.superficie + 18 * (X.aillament == 'baix') + rng.normal(0, 5, len(X))
    X.loc[rng.choice(len(X), 20, replace=False), 'superficie'] = np.nan
    (train, test, yt, ytest) = train_test_split(X, y, test_size=0.2, random_state=42)
    (train, valid, yt, yv) = train_test_split(train, yt, test_size=0.25, random_state=42)

    def make(estimator):
        # La imputació i l’escala s’ajusten dins del pipeline, només amb entrenament.
        numeric = Pipeline([('impute', SimpleImputer(strategy='median')), ('scale', StandardScaler())])
        prep = ColumnTransformer([('num', numeric, ['superficie']), ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), ['aillament'])])
        return Pipeline([('prep', prep), ('model', estimator)])
    candidates = {'dummy': make(DummyRegressor()), 'ridge': make(Ridge(alpha=1)), 'forest': make(RandomForestRegressor(n_estimators=80, min_samples_leaf=5, random_state=42, n_jobs=1))}
    metrics = {}
    for (name, model) in candidates.items():
        model.fit(train, yt)
        metrics[name] = mean_absolute_error(yv, model.predict(valid))
    # La selecció usa exclusivament validació; la prova es consulta després.
    chosen = min(metrics, key=metrics.get)
    print('MAE validació:', metrics)
    print('Triat:', chosen)
    print('MAE test reservat:', mean_absolute_error(ytest, candidates[chosen].predict(test)))
    assert min(metrics.values()) < metrics['dummy']
    out = Path(__file__).resolve().parent / 'eixides'
    out.mkdir(exist_ok=True)
    pd.DataFrame({'real': ytest, 'prediccio': candidates[chosen].predict(test)}).to_csv(out / 'prova.csv', index=False)
    print('Categoria nova:', candidates[chosen].predict(pd.DataFrame({'superficie': [85.0], 'aillament': ['mitja']})))
if __name__ == '__main__':
    main()
