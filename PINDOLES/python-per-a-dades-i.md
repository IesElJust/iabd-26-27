---
title: Python Per A Dades I
---

# Python Per A Dades I

## Objectiu de la píndola

Ací baixem a ús real de `NumPy` i `Pandas`, que són la base de quasi tot el treball de dades del curs.

La idea no és memoritzar totes les funcions, sino entendre què resol cada llibreria.

## Com repartir els papers

- `NumPy`: arrays i càlcul numèric
- `Pandas`: taules, columnes, neteja i transformació de dades

La distinció és important perquè a principiants els dos paquets els poden paréixer "llibreries per a dades" sense més. Però no resolen exactament el mateix problema.

- `NumPy` és especialment fort quan treballem amb estructura numèrica homogènia i càlcul eficient
- `Pandas` és especialment fort quan treballem amb taules reals, columnes heterogènies, nuls i preguntes de negoci

## Pensar `NumPy`

Un array de `NumPy` és útil quan treballem amb valors numèrics i volem fer càlcul vectoritzat.

```python
import numpy as np

lectures = np.array([18.2, 19.1, 21.4])
mitjana = lectures.mean()
```

La idea de fons és que `NumPy` permet operar sobre col·leccions de valors d'una forma més pròxima a les matemàtiques i menys a un bucle manual línia per línia.

No sempre l'alumnat el veurà de manera explícita, però moltes eines de dades i ML es recolzen en esta lògica matricial.

## Pensar `Pandas`

`Pandas` és la ferramenta central quan tenim fitxers tabulars, registres o datasets de negoci.

```python
import pandas as pd

df = pd.read_csv("sales_history.csv")
df["marge"] = df["ingressos"] - df["cost"]
```

La potència real de `Pandas` és que permet pensar una taula no només com un fitxer, sinó com un espai de treball on podem:

- descriure qualitat
- transformar columnes
- resumir patrons
- preparar la base per a modelar o visualitzar

## Per què esta capa és tan central al curs

Moltes vegades l'alumnat pensa que el centre del treball està en el model. Però en la pràctica, la major part del temps s'invertix en:

- entendre dades
- netejar valors
- revisar tipus
- crear variables útils
- resumir patrons

Per això `NumPy` i `Pandas` no són un pròleg. Són una part molt gran del treball real.

## Operacions mínimes que sí hem de saber fer

- carregar un CSV
- mirar columnes i tipus
- detectar nuls
- filtrar files
- crear una columna derivada
- agrupar i resumir

També convé arribar a entendre què significa cada una.

- carregar un CSV: passar d'un fitxer a una taula manipulable
- mirar tipus: detectar si hi ha números, textos o camps mal interpretats
- detectar nuls: localitzar pèrdues de qualitat
- filtrar files: quedar-se amb una part rellevant del problema
- crear una columna derivada: transformar dades crues en informació més útil
- agrupar i resumir: començar a llegir patrons col·lectius i no només casos individuals

## Exemple teòric curt: dada crua vs dada treballable

Imaginem una taula de vendes amb estes columnes:

- `ingressos`
- `cost`
- `canal`
- `devolucions`

La dada crua només informa que eixos camps existixen.

Quan afegim:

- `marge = ingressos - cost`
- una agrupació per `canal`
- una lectura de devolucions mitjanes

ja estem convertint dada en estructura de decisió.

## Exemple guiat de classe

Situació:

en `Predicció Comercial`, volem saber quins canals tenen més devolucions.

```python
resum = (
    df.groupby("canal")["devolucions"]
    .mean()
    .sort_values(ascending=False)
)
```

Ací l'alumnat ha d'entendre dos coses:

- que la dada encara s'està llegint, no jutjant
- que una taula resum pot orientar molt abans d'entrenar cap model

I encara una tercera:

- que una bona lectura agregada ja pot donar valor de negoci encara que no hi haja cap model predictiu darrere

## Error habitual

Saltar massa ràpid al modelatge sense revisar abans tipus, nuls o columnes mal codificades.

També és habitual:

- encadenar moltes transformacions sense entendre cada pas
- no conservar una columna original abans de transformar-la
- barrejar neteja, càlcul i conclusions sense ordre

Per això convé que el notebook faça visible el fil:

1. què tenim
2. què està mal o és dubtós
3. què transformem
4. què aprenem després de transformar

## Pràctica guiada suggerida

Situació:

agafeu un dataset de vendes o d'incidents i feu quatre blocs explícits:

1. tipus i valors nuls
2. correccions o exclusions
3. columna derivada útil
4. resum agrupat que permeta una lectura inicial

Al final, l'alumnat hauria d'escriure una conclusió curta:

`abans de modelar, ja hem vist que...`

Esta frase és molt valuosa perquè obliga a entendre que el treball de dades no comença en el model, sinó abans.

## Mini pràctica

Pregunta:

si vols calcular la mitjana de vendes per segment i comparar-la, quin paquet t'ajuda més directament?

## Solució orientativa

`Pandas`, perquè estem treballant amb dades tabulars i agrupacions per columna.

## Resum final

`NumPy` i `Pandas` no són un extra. Són la capa operativa que connecta fitxers, exploració, modelatge i explicació.

Quan esta capa és sòlida, l'alumnat deixa de dependre tant de receptes i comença a entendre de veritat què està fent amb les dades.

## Com usar-la en estos projectes

- BiciTierra Market: lectura, neteja, agrupació i preparació del dataset
- P3: validació simple de lectures i agregacions temporals bàsiques
- P5: consolidació de dades abans de passar a analítica o integració

## Vegeu també

- `Python i Entorns`
- `EDA i Qualitat de Dades`
- `Visualitzacio amb Matplotlib i Seaborn`
- `Scikit-Learn Introductori`
