"""Dades menudes d'un servei tècnic i totals per comprovar manualment Power BI."""
from pathlib import Path
import pandas as pd

def main():
    out = Path(__file__).resolve().parent / 'eixides'
    out.mkdir(exist_ok=True)
    # Una fila representa una incidència: esta és la granularitat.
    facts = pd.DataFrame({'id': [1, 2, 3, 4], 'data': ['2026-01-01', '2026-01-02', '2026-02-01', '2026-02-02'], 'servei_id': [1, 1, 2, 2], 'minuts': [20, 40, 60, 80], 'resolt': [1, 0, 1, 1]})
    # El catàleg té una clau única per servei.
    dim = pd.DataFrame({'servei_id': [1, 2], 'servei': ['Web', 'Correu']})
    facts.to_csv(out / 'incidencies.csv', index=False)
    dim.to_csv(out / 'serveis.csv', index=False)
    # Els totals menuts permeten contrastar després el dashboard a mà.
    assert facts.id.nunique() == 4 and facts.minuts.sum() == 200
    print('Controls esperats: 4 incidències; 200 minuts; mitjana 50; resolució 75%.')
    print('Filtre Web: 2 incidències; 60 minuts; mitjana 30; resolució 50%.')
    print('Filtre Correu: 2 incidències; 140 minuts; mitjana 70; resolució 100%.')
if __name__ == '__main__':
    main()
