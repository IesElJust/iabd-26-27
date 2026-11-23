---
title: "Clustering i interpretació de perfils"
description: "Fonaments, exemples reproduïbles i pràctica progressiva: clustering i interpretació de perfils."
tags: [IABD, dades, formació]
icon: material/book-open-page-variant
status: ampliada
---

# 08 · Clustering i interpretació de perfils

[← Índex de les píndoles](../index.md)

!!! abstract "Què aprendràs"
    - Construir una matriu de característiques amb una fila per entitat.
    - Comparar agrupacions amb mètriques i perfils.
    - Examinar estabilitat i limitacions de les etiquetes.

**Coneixements previs:** pandas, escales numèriques i gràfics de dispersió.

**Dedicació orientativa:** 3–4 h per a lectura i laboratori guiat; les extensions i els exercicis autònoms requerixen temps addicional.

!!! tip "Dos recorreguts possibles"
    **Essencial:** llig els fonaments, executa el laboratori i completa la pràctica inicial. **Aprofundiment:** continua amb les pràctiques intermèdia i avançada i els exercicis. El professorat pot seleccionar-les segons els coneixements previs; no són totes obligatòries dins del projecte.

## Mapa de la unitat

Agrupar no és descobrir etiquetes inevitables → Triar variables i escales → K-Means pas a pas → Escollir el nombre de grups → DBSCAN i densitat → PCA i representació → Estabilitat i assignació de casos nous → Perfils que ajuden a decidir

## 1. Agrupar no és descobrir etiquetes inevitables

El clustering agrupa observacions segons una noció de semblança. A diferència de la classificació supervisada, normalment no partim d’una etiqueta de resposta que el model haja d’imitar. Les agrupacions depenen de les variables, l’escala, la distància i l’algorisme.

En una biblioteca podem agrupar persones per freqüència de visites, duració i recència. Una segmentació per interessos culturals podria donar grups diferents. Cap de les dos és «la partició real» de les persones; cada una respon una pregunta.

Segmentar inclou, a més d’agrupar, interpretar i decidir com s’utilitzaran els perfils. Un algorisme pot separar punts geomètricament i produir grups sense utilitat operativa.

## 2. Triar variables i escales

Un identificador pot ser numèric, però la diferència entre dos identificadors no representa una distància de comportament. Exclou-lo de la geometria. Una data comuna tampoc aporta separació útil.

Si es combinen euros, dies i nombres de visites sense escala, una magnitud pot dominar la distància pel seu rang. L’estandardització transforma cada variable amb la seua mitjana i desviació. És una opció, no una garantia: davant d’extrems forts pot convenir una escala robusta o una transformació justificada.

Variables redundants poden duplicar una mateixa informació. Si despesa = freqüència × tiquet, incorporar les tres sense reflexió modifica el pes implícit del valor monetari. Tria segons la pregunta i compara com canvia el resultat.

## 3. K-Means pas a pas

K-Means busca centres que reduïsquen la suma de distàncies quadràtiques de cada punt al centre assignat. De manera simplificada, inicialitza centres, assigna punts al més pròxim, recalcula centres i repetix fins a convergir.

Funciona especialment bé amb grups compactes en una geometria euclidiana. Pot dividir un grup allargat o combinar grups de densitat desigual. També és sensible a escala i a valors extrems.

```python title="Una agrupació mínima"
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

X = [[1, 10], [2, 12], [1, 8], [8, 70], [9, 75], [7, 68]]
z = StandardScaler().fit_transform(X)
model = KMeans(n_clusters=2, n_init=10, random_state=42).fit(z)
print(model.labels_)
```

Els números de grup són identificadors arbitraris. El grup 0 d’una execució no és necessàriament el grup 0 d’una altra. Per comparar particions, usa una mesura que no depenga dels noms, com l’índex de Rand ajustat.

## 4. Escollir el nombre de grups

La inèrcia disminuïx quan augmenta `k`; el mètode del colze busca una reducció amb rendiments decreixents, però no sempre hi ha un colze clar. La silueta compara proximitat al grup propi amb separació del grup alternatiu més pròxim.

Una silueta alta pot ajudar a identificar separació, però no demostra utilitat comercial ni correcció social d’una segmentació. A més, algunes geometries que resulten útils no maximitzen esta mètrica.

Compara un rang raonable, revisa grandàries, estabilitat i interpretació. Un grup de dos casos pot representar una anomalia interessant o un artefacte. Cal veure els registres, no només l’índex global.

## 5. DBSCAN i densitat

DBSCAN connecta regions de densitat a partir d’un radi `eps` i d’un mínim de punts. Pot identificar formes no esfèriques i marcar observacions com a soroll, habitualment amb etiqueta `-1`.

No requerix fixar el nombre de grups, però sí paràmetres que depenen de l’escala i la densitat. Amb un radi massa menut, molts punts queden com a soroll; amb un massa gran, els grups es fusionen. En densitats molt diferents, un únic radi pot ser inadequat.

El soroll no és necessàriament un client defectuós ni una observació eliminable. Significa que l’algorisme no l’ha inclòs en una regió densa amb eixos paràmetres. Descriu la decisió sense convertir-la en un judici sobre la persona.

## 6. PCA i representació

L’anàlisi de components principals, PCA, transforma variables en direccions que expliquen variància. Pot ajudar a visualitzar una matriu de moltes dimensions en dos eixos. No és un algorisme de clustering i no preserva automàticament totes les distàncies rellevants.

Una vista en dos components pot amagar solapament o separació present en altres dimensions. Reporta la variància explicada i interpreta els perfils amb les variables originals, no només amb la posició en un dibuix.

Si s’usa PCA abans d’agrupar, s’ha canviat l’espai sobre el qual es definix semblança. Justifica per què es fa i compara amb una alternativa més simple.

## 7. Estabilitat i assignació de casos nous

Canviar la llavor comprova sensibilitat a la inicialització; canviar la mostra comprova una qüestió distinta. Una partició estable entre dos llavors pot continuar sent fràgil si s’exclou un grup de dades o canvia l’escala.

K-Means permet assignar punts nous als centres ja ajustats mitjançant `predict`. Això no refà els centres. DBSCAN, en la implementació habitual de scikit-learn, no oferix un `predict` equivalent: no s’ha de prometre una assignació automàtica futura sense definir un procediment.

Conserva el preprocessament ajustat. Tornar a escalar cada lot nou amb la seua pròpia mitjana canvia la geometria i deixa de ser la mateixa segmentació.

## 8. Perfils que ajuden a decidir

Per cada segment, descriu nombre i proporció d’observacions, mediana o mitjana de variables útils, dispersió i casos que no encaixen en una lectura simple. Posa un nom descriptiu, com «visita freqüent i curta», en lloc d’inferir motivacions personals no observades.

Una acció suggerida ha d’incloure una hipòtesi comprovable. «Provar un horari ampliat per a visites llargues» és una proposta que es pot avaluar; «este grup és fidel» pot excedir el que mesuren tres variables.

El laboratori genera 270 perfils sintètics de biblioteca i compara K-Means, estabilitat entre llavors, DBSCAN i una projecció PCA. La mescla de partida facilita l’experiment, però les etiquetes latents no s’utilitzen com a resposta. El treball consisteix a justificar una lectura, no a endevinar els números del generador.

## Laboratori complet i reproduïble

**Context:** treballarem amb dades sintètiques creades pel mateix programa. No cal descarregar datasets ni usar els CSV de BiciTierra. Els valors servixen per aprendre i comprovar procediments; no descriuen una població real.

**Materials:** Python 3.10 o superior, un entorn virtual i els [requisits de la unitat](requirements.txt). Consulta la [preparació comuna](../index.md) abans d’instal·lar-los.

Des de la carpeta d’esta píndola, amb l’entorn activat:

```bash
python -m pip install -r requirements.txt
python codi/exemple.py
```

El programa crea `codi/eixides/`. Pots examinar les eixides sense modificar el codi original. Per resoldre les variants, treballa sobre una còpia i actualitza les comprovacions quan canvies deliberadament les dades.

### Exemple comentat

[Obri o descarrega el programa complet](codi/exemple.py){ download="exemple.py" }. Cada comprovació `assert` expressa una propietat esperada de les dades de demostració; si falla, investiga la causa abans d’eliminar-la.

```python title="codi/exemple.py" linenums="1"
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
```

## Pràctiques guiades

Cada pràctica deixa una evidència petita: una eixida comprovada i una explicació de la decisió. Els temps són orientatius i no inclouen instal·lació.

### Pràctica 1 · Preparar perfils comparables

**Nivell i temps:** Inicial · 20–30 min.

**Objectiu:** Entendre l’efecte de les unitats abans de calcular distàncies.

**Materials:** exemple comentat d’esta unitat, les seues eixides i una còpia de treball per a les modificacions.

**Procediment:**

1. Executa l’exemple i descriu les tres variables d’ús de biblioteca.
2. Compara rangs originals de visites, minuts i dies d’absència.
3. Localitza l’estandardització i comprova mitjanes aproximades zero i desviacions poblacionals aproximades u.
4. Relaciona cada fila amb una persona sintètica i descarta identificadors com a variables de distància.

!!! success "Comprovació i evidència esperada"
    La matriu usada en clustering té 270 files i tres característiques escalades.

**Preguntes de reflexió:**

- Per què una variable amb rang més gran pot dominar la distància?
- Què significa una coordenada negativa després d’escalar?
- Quina informació es perdria eliminant una variable sense revisar-la?

**Ampliació opcional:** Compara una agrupació sense escalar i explica quina variable sembla dominar-la.

### Pràctica 2 · Triar una agrupació exploratòria

**Nivell i temps:** Intermèdia · 30–45 min.

**Objectiu:** Combinar silhouette amb interpretació dels perfils.

**Materials:** exemple comentat d’esta unitat, les seues eixides i una còpia de treball per a les modificacions.

**Procediment:**

1. Registra els resultats per a k entre 2 i 5.
2. Revisa el k seleccionat pel màxim de silhouette sense anomenar-lo nombre real de grups.
3. Calcula mida, mitjana i mediana de cada perfil en unitats originals.
4. Proposa noms descriptius basats en comportaments observats i una possible utilitat per al servei bibliotecari.

!!! success "Comprovació i evidència esperada"
    Cada nom es justifica amb valors i no expressa un judici sobre el valor de les persones.

**Preguntes de reflexió:**

- Què mesura silhouette i què no mesura?
- Per què dues agrupacions poden ser útils per a preguntes diferents?
- Quin risc té donar un nom massa categòric a un grup?

**Ampliació opcional:** Compara els perfils amb k immediatament inferior i descriu quin grup s’ha fusionat.

### Pràctica 3 · Estabilitat i punts sense grup

**Nivell i temps:** Avançada · 45–60 min.

**Objectiu:** Examinar dependència de la inicialització i del model d’agrupació.

**Materials:** exemple comentat d’esta unitat, les seues eixides i una còpia de treball per a les modificacions.

**Procediment:**

1. Compara les etiquetes de dues llavors mitjançant ARI, sense exigir que els números de grup coincidisquen.
2. Revisa el resultat de DBSCAN i separa grups de l’etiqueta −1.
3. Varia `eps` en una còpia i registra nombre de grups i punts de soroll.
4. Explica per què una projecció PCA de dues dimensions pot ocultar separacions presents en tres.

!!! success "Comprovació i evidència esperada"
    L’informe distingix estabilitat de llavors, sensibilitat de densitat i limitació de projecció.

**Preguntes de reflexió:**

- Per què comparar números d’etiqueta fila a fila pot ser enganyós?
- Un punt marcat com a soroll és necessàriament una dada incorrecta?
- Per què estabilitat no equival a utilitat?

**Ampliació opcional:** Repetix l’anàlisi en una submostra i compara perfils, mantenint explícita la població que s’ha exclòs.

## Exercicis autònoms

Intenta resoldre cada repte abans de desplegar l’orientació. Es valora el raonament i les comprovacions, no només obtindre una xifra.

### Repte 1 · Etiquetes permutades

Compara dos resultats idèntics que anomenen els grups 0/1 i 1/0.

??? example "Solució orientativa i criteri de revisió"
    La partició és la mateixa encara que cap número coincidisca. Una mètrica com ARI té en compte la pertinença compartida i no exigix la mateixa numeració.

### Repte 2 · Un identificador numèric

Argumenta per què no has d’escalar i incloure automàticament el número de carnet en les distàncies.

??? example "Solució orientativa i criteri de revisió"
    Que siga numèric no li dóna un significat quantitatiu. La proximitat entre números de carnet no representa necessàriament similitud de comportament.

### Repte 3 · Del perfil a l’acció

Proposa una acció de servei per a un perfil i una manera d’avaluar-la.

??? example "Solució orientativa i criteri de revisió"
    Per exemple, oferir informació d’horaris a usuaris amb absències llargues i mesurar resposta amb un disseny adequat. El cluster no prova per si mateix la causa de l’absència ni l’efecte de l’acció.

## Errors habituals i diagnòstic

| Símptoma | Causa que convé investigar | Comprovació o correcció |
|---|---|---|
| Un grup domina l’espai | Escales molt diferents o variable irrellevant. | Revisa unitats i selecció abans de canviar k. |
| Canvien els números de grup | Permutació d’etiquetes. | Compara pertinença amb ARI i perfils. |
| DBSCAN marca quasi tot com soroll | Paràmetres de densitat inadequats per l’escala. | Revisa distàncies, eps i min_samples sense forçar un nombre de grups. |

## Autoavaluació i evidències

Abans de donar la unitat per treballada, comprova estos punts i escriu una frase d’evidència per a cadascun:

- [ ] Puc construir una matriu de característiques amb una fila per entitat.
- [ ] Puc comparar agrupacions amb mètriques i perfils.
- [ ] Puc examinar estabilitat i limitacions de les etiquetes.
- [ ] He executat el laboratori i he contrastat almenys un resultat independentment.
- [ ] Puc explicar una limitació i un cas en què el procediment requeriria canvis.

**Lliurable de la píndola:** còpia de treball reproduïble, resultats de la pràctica seleccionada i un text breu que indique pregunta, decisió, comprovació i limitació. Si s’usa dins de BiciTierra Market, integra esta evidència en el lliurable setmanal corresponent; no cal crear una entrega duplicada.

## Fonts per aprofundir

- [Documentació oficial de referència](https://scikit-learn.org/stable/modules/clustering.html). Consulta especialment els conceptes i els supòsits descrits en la unitat.

Les versions executades i els límits de la comprovació estan en el [registre de validació](../VALIDACIO.md). Els exemples són originals i les dades són sintètiques.

## Aplicació final a BiciTierra Market

**Moment orientatiu:** setmana 4. Esta correspondència ajuda a triar materials i no substituïx el document de treball de l’alumnat.

Construïx perfils de customers.csv amb variables justificades i una fila per client. Exclou identificadors de les distàncies. Lliura mides, valors representatius, estabilitat i una interpretació prudent abans de proposar accions comercials.

**Transferència:** identifica quin concepte acabes de practicar, quina dada del projecte l’exigix i què has de canviar respecte del laboratori. Justifica eixa adaptació abans de copiar codi.
