"""Perfils sintètics d'ús d'una biblioteca. Les etiquetes no són veritat externa."""
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score, adjusted_rand_score
from sklearn.decomposition import PCA

def main():
    rng = np.random.default_rng(14)
    centers = [(2, 15, 60), (7, 60, 10), (4, 100, 25)]
    data = np.vstack([rng.normal(c, [1, 12, 8], size=(90, 3)) for c in centers])
    df = pd.DataFrame(np.maximum(data, 0), columns=['visites_mes', 'minuts_visita', 'dies_absencia'])
    # Escalem perquè minuts, visites i dies no dominen només per unitats.
    scaler = StandardScaler()
    z = scaler.fit_transform(df)
    scores = {}
    models = {}
    for k in range(2, 6):
        models[k] = KMeans(n_clusters=k, n_init=10, random_state=42).fit(z)
        scores[k] = silhouette_score(z, models[k].labels_)
    # La selecció per silhouette és exploratòria, no una veritat externa.
    k = max(scores, key=scores.get)
    labels = models[k].labels_
    # ARI compara particions encara que els números d’etiqueta canvien.
    replica = KMeans(n_clusters=k, n_init=10, random_state=9).fit_predict(z)
    print('Silhouette:', scores, 'k exploratori:', k)
    print('Estabilitat entre llavors (ARI):', adjusted_rand_score(labels, replica))
    df['grup'] = labels
    print(df.groupby('grup').mean().round(2).to_string())
    # −1 representa soroll de DBSCAN, no un grup addicional.
    db = DBSCAN(eps=0.65, min_samples=8).fit_predict(z)
    print('DBSCAN: grups', len(set(db) - {-1}), 'soroll', int((db == -1).sum()))
    coords = PCA(n_components=2).fit_transform(z)
    assert coords.shape == (270, 2) and df.grup.nunique() == k
    out = Path(__file__).resolve().parent / 'eixides'
    out.mkdir(exist_ok=True)
    df.to_csv(out / 'perfils.csv', index=False)
if __name__ == '__main__':
    main()
