"""Informe gràfic local; no descarrega datasets."""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # La llavor fixa fa repetible esta simulació docent.
    rng = np.random.default_rng(42)
    df = pd.DataFrame({'temperatura': rng.normal(20, 5, 180), 'edifici': np.repeat(['A', 'B', 'C'], 60)})
    df['kwh'] = 40 + 2.5 * abs(df.temperatura - 19) + df.edifici.map({'A': 0, 'B': 8, 'C': -3}) + rng.normal(0, 3, len(df))
    sns.set_theme(style='whitegrid')
    (fig, axes) = plt.subplots(1, 3, figsize=(14, 4), layout='constrained')
    sns.histplot(data=df, x='kwh', bins=18, ax=axes[0], color='#315b8a')
    sns.boxplot(data=df, x='edifici', y='kwh', ax=axes[1], color='#b5cbe0')
    sns.scatterplot(data=df, x='temperatura', y='kwh', hue='edifici', style='edifici', ax=axes[2])
    axes[0].set(xlabel='Consum diari (kWh)', ylabel='Dies', title='Distribució del consum')
    axes[1].set(xlabel='Edifici', ylabel='Consum diari (kWh)', title='Diferències entre edificis')
    axes[2].set(xlabel='Temperatura (°C)', ylabel='Consum diari (kWh)', title='Temperatura i consum')
    out = Path(__file__).resolve().parent / 'eixides'
    out.mkdir(exist_ok=True)
    # Exportem abans de tancar per conservar tots els elements de la figura.
    fig.savefig(out / 'energia.png', dpi=140)
    # Exportem abans de tancar per conservar tots els elements de la figura.
    fig.savefig(out / 'energia.svg')
    plt.close(fig)
    df.to_csv(out / 'energia.csv', index=False)
    assert (out / 'energia.png').stat().st_size > 1000
    print(df.groupby('edifici').kwh.agg(['count', 'mean', 'median']).round(2).to_string())
if __name__ == '__main__':
    main()
