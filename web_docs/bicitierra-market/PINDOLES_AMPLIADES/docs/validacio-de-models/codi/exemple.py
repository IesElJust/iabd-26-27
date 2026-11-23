"""Backtesting per dates completes d'un panell de dos edificis."""
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error

def main():
    rng = np.random.default_rng(7)
    dates = pd.date_range('2023-01-01', periods=48, freq='MS')
    rows = []
    for (building, offset) in [('A', 0), ('B', 30)]:
        for (i, date) in enumerate(dates):
            rows.append({'data': date, 'edifici': building, 't': i, 'consum': 100 + offset + i * 0.8 + 12 * np.sin(2 * np.pi * i / 12) + rng.normal(0, 3)})
    df = pd.DataFrame(rows).sort_values(['edifici', 'data'])
    # Retards dins de cada edifici; les sèries són mensuals completes.
    df['lag1'] = df.groupby('edifici').consum.shift(1)
    df['lag12'] = df.groupby('edifici').consum.shift(12)
    df = df.dropna().copy()
    df['b'] = (df.edifici == 'B').astype(int)
    # lag1 pressuposa predicció successiva d’un mes, no sis mesos de colp.
    features = ['lag1', 'lag12', 't', 'b']
    # Els talls són per mesos complets, no per posició de fila.
    folds = [('2024-12-01', '2025-01-01', '2025-06-01'), ('2025-06-01', '2025-07-01', '2025-12-01')]
    results = []
    for (end, start, stop) in folds:
        tr = df[df.data <= end]
        va = df[df.data.between(start, stop)]
        assert tr.data.max() < va.data.min() and set(tr.data).isdisjoint(set(va.data))
        model = Ridge(alpha=1).fit(tr[features], tr.consum)
        results.append({'train_end': end, 'valid_start': start, 'files': len(va), 'mae_model': mean_absolute_error(va.consum, model.predict(va[features])), 'mae_lag12': mean_absolute_error(va.consum, va.lag12)})
    print(pd.DataFrame(results).round(3).to_string(index=False))
    # 2026 queda reservat: alpha s’ha fixat abans d’esta avaluació.
    train = df[df.data < '2026-01-01']
    test = df[df.data >= '2026-01-01']
    model = Ridge(alpha=1).fit(train[features], train.consum)
    pred = model.predict(test[features])
    mae = mean_absolute_error(test.consum, pred)
    wape = 100 * np.abs(test.consum - pred).sum() / np.abs(test.consum).sum()
    print(f'Test: MAE={mae:.3f}; WAPE={wape:.3f}%')
    out = Path(__file__).resolve().parent / 'eixides'
    out.mkdir(exist_ok=True)
    pd.DataFrame(results).to_csv(out / 'backtesting.csv', index=False)
    assert len(test) == 24 and len(results) == 2
if __name__ == '__main__':
    main()
