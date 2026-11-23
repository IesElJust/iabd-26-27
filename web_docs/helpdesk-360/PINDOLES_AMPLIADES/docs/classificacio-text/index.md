# Classificació de text · Complement de scikit-learn

[Índex](../index.md)

## Punt de partida i objectiu

En P2 ja heu treballat `fit`, `predict`, pipelines i separació d'entrenament i prova. Ací aplicareu eixos coneixements a text lliure. En acabar podreu explicar què aprén un vectoritzador, per què una frase nova pot quedar sense representació i com comparar una classificació de tickets amb regles.

La lectura i la pràctica inicial requerixen aproximadament dos hores. Necessiteu Python, pandas i scikit-learn en l'entorn de notebooks del projecte. El [laboratori descarregable](laboratori.py) usa frases sintètiques independents del CSV del projecte: comprova la mecànica, no estima la qualitat del pilot.

## Del text a una matriu

Un estimador lineal no rep directament una frase. El vectoritzador aprén un vocabulari d'entrenament i construïx una columna per terme. TF mesura presència o freqüència dins d'un text; IDF reduïx el pes dels termes estesos pel corpus d'ajust. TF-IDF no és comprensió semàntica: dues frases equivalents sense vocabulari compartit poden quedar lluny.

`TfidfVectorizer` combina tokenització, vocabulari i ponderació. Amb `strip_accents='unicode'` podeu reduir diferències de grafia, però heu de valorar si perdeu distincions útils. Els bigrames incorporen parelles consecutives com «quota plena»; amplien el vocabulari i poden sobreajustar un conjunt menut. No elimineu automàticament negacions com «no».

Un terme que no existia en entrenament no crea una columna nova en predicció. Si tots els termes d'un ticket són desconeguts, el vector pot quedar a zero i el classificador encara pot retornar una categoria pel seu intercept. Una etiqueta retornada no demostra que el model haja entés la consulta.

La [referència de TF-IDF](https://scikit-learn.org/stable/modules/feature_extraction.html) descriu la ponderació i les limitacions de les representacions per freqüències.

## Aprendre només amb entrenament

El vocabulari i IDF també són paràmetres apresos. Si vectoritzeu tots els tickets abans de separar, la prova influïx en la representació. Poseu vectoritzador i estimador en el mateix `Pipeline` i ajusteu-lo només amb entrenament.

```python
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

model = make_pipeline(
    TfidfVectorizer(strip_accents='unicode', ngram_range=(1, 2)),
    LogisticRegression(max_iter=1000, random_state=42),
)
# X_train és una seqüència de textos; y_train, les categories revisades.
# model.fit(X_train, y_train)
```

Una categoria de departament no equival a una urgència. Feu primer la classificació de departament; tracteu la prioritat amb criteris específics i no useu l'etiqueta objectiu entre els predictors.

## Laboratori guiat

Descarregueu el programa i executeu `python laboratori.py`. Observeu el suport de cada classe en l'informe i les files de la matriu de confusió: representen categories reals; les columnes representen prediccions. El programa també comprova un text amb vocabulari absent.

Canvieu una frase de prova per una paràfrasi sense paraules compartides. Observeu si baixa el nombre de termes reconeguts i si la predicció continua apareixent. Escriviu per què això és possible abans de modificar l'entrenament. Després d'eixa inspecció, el conjunt ja és de desenvolupament, no una prova final independent.

F1 macro calcula F1 per classe i després en fa la mitjana sense ponderar pel volum. Accuracy pot amagar una classe minoritària. Mostreu les dues mètriques, el suport i els errors; un únic error sobre pocs tickets pot canviar molt els percentatges.

## Pràctica en el projecte

En la pràctica inicial, executeu el laboratori i expliqueu el vector zero i un error. En la intermèdia, seguiu la [comparació del projecte](../../../MATERIALS_PRACTICS/notebooks/03_comparacio_models.md) amb el CSV revisat, agrupant quasi duplicats abans de separar. Compareu regles i model sobre els mateixos IDs.

En l'extensió, compareu unigrames i bigrames amb dades de desenvolupament, deixant la prova final intacta. Registreu configuració, particions i resultat. Si afegiu un llindar de confiança, calibreu-lo a banda: `predict_proba` no és una garantia d'encert i no s'ha de confondre amb cobertura documental.

## Exercicis i comprovació

Expliqueu per què afegir una paraula només a prova no modifica el vocabulari. Descriviu què passaria si dos tickets quasi iguals acabaren en particions distintes. Finalment, decidiu què ha de fer el sistema amb un text sense termes reconeguts: derivar és una opció explícita, i s'ha de comptar entre els resultats de la prova.

Una resposta correcta distingix vocabulari d'entrenament, representació de prova i decisió del classificador. L'evidència és el laboratori executat, la comparativa i una lectura d'errors; no és suficient mostrar un percentatge sense suport.
