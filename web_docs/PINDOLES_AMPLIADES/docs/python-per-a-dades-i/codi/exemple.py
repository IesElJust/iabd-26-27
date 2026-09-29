"""Taules i arrays: unió controlada d'incidències amb serveis."""
from pathlib import Path
import numpy as np
import pandas as pd

def main():
    temps = np.array([20.0, 30.0, 50.0])
    assert temps.shape == (3,)
    print('Minuts a hores:', temps / 60)
    incidencies = pd.DataFrame({'id': [1, 2, 3, 4, 5], 'servei': ['web', 'web', 'correu', 'correu', 'vpn'], 'minuts': [20.0, 30.0, None, 50.0, 10.0], 'data': ['2026-01-01', '2026-01-03', '2026-02-01', '2026-02-03', '2026-02-04']})
    serveis = pd.DataFrame({'servei': ['web', 'correu'], 'responsable': ['Equip A', 'Equip B']})
    incidencies['data'] = pd.to_datetime(incidencies['data'], format='%Y-%m-%d')
    # Exigim una sola coincidència de catàleg per incidència.
    resultat = incidencies.merge(serveis, on='servei', how='left', validate='many_to_one', indicator=True)
    assert len(resultat) == 5
    assert (resultat['_merge'] == 'left_only').sum() == 1
    # size compta files; count només valors no absents.
    resum = resultat.groupby('servei', dropna=False).agg(files=('id', 'size'), observades=('minuts', 'count'), mitjana=('minuts', 'mean'))
    # min_count evita presentar absència completa com a suma zero.
    mensual = incidencies.set_index('data')['minuts'].resample('MS').sum(min_count=1)
    out = Path(__file__).resolve().parent / 'eixides'
    out.mkdir(exist_ok=True)
    resultat.to_csv(out / 'incidencies.csv', index=False)
    resum.to_csv(out / 'resum-serveis.csv')
    print(resum.to_string())
    print('Totals mensuals observats:\n', mensual)
    print('Nuls conservats:', resultat.minuts.isna().sum())
if __name__ == '__main__':
    main()
