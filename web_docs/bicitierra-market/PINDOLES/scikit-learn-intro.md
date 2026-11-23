---
title: Scikit-Learn Introductori
---

# Scikit-Learn Introductori

## Què aporta de veritat

`scikit-learn` permet muntar un pipeline de modelatge clàssic de manera ràpida i bastant coherent.

És especialment útil per a:

- preprocessament
- partició train/test
- models baseline
- mètriques
- comparació d'alternatives

La gran virtut de `scikit-learn` en context docent és que obliga a pensar el modelatge com un procés ordenat i no com una successió improvisada de proves.

## Pipeline mínim que cal entendre

1. preparar dades
2. separar `features` i `target`
3. fer `train_test_split`
4. entrenar un model base
5. avaluar-lo

Este pipeline és més important que qualsevol model concret. Si l'alumnat entén bé esta seqüència, després podrà canviar de model amb molt més criteri.

## Què és realment una baseline

Una baseline no és "el model final però més simple".

És una referència inicial que ens permet respondre:

- estem millorant o no?
- el problema sembla abordable amb esta informació?
- les dades tenen una estructura aprofitable?

Per això una baseline modesta però ben llegida és molt més valuosa que un model més complex mal justificat.

## Separar dades i evitar autoengany

La divisió `train/test` no és un tràmit tècnic. És una manera d'evitar que el model es jutge sobre els mateixos exemples amb què ha après.

Sense esta separació, el model pot paréixer molt bo i ser en realitat molt fràgil fora del notebook.

## Exemple curt

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print(classification_report(y_test, pred))
```

La lectura docent d'este exemple no és "ja sabem usar `RandomForest`". La lectura és:

- hem separat dades
- hem entrenat un model reproducible
- hem obtingut una eixida d'avaluació llegible

És una porta d'entrada clara al treball seriós.

## Què ha d'entendre l'alumnat

- que la baseline és un punt de partida, no una excusa per tancar el problema massa prompte
- que una mètrica solta no basta
- que sense bon preprocessament és fàcil tindre resultats enganyosos

També convé que entenga:

- que una millora petita però coherent pot ser més valuosa que una gran millora dubtosa
- que el model no es jutja només per encert, sinó per lectura, estabilitat i utilitat

## Mètriques: no totes conten la mateixa història

Segons el problema, no és igual mirar:

- `accuracy`
- `precision`
- `recall`
- `F1`

En alguns contextos, fallar una alerta greu és pitjor que llançar alguna falsa alarma. En altres, saturar d'alertes també és un problema.

Per això la mètrica ha de connectar amb l'impacte del cas d'ús, no només amb la facilitat de càlcul.

## Quan encaixa molt bé al curs

- classificació de tickets o incidències
- predicció comercial
- detecció simple de risc
- segmentació inicial

## Error habitual

Canviar de model una vegada i una altra sense controlar primer la qualitat de les dades, el tall train/test o la lectura de les mètriques.

També és habitual:

- comparar models entrenats sobre preparacions diferents sense documentar-ho bé
- presentar el millor resultat sense explicar per què és millor
- confondre segmentació no supervisada amb classificació supervisada

## Exemple guiat de classe

Situació:

en `Predicció Comercial`, dos grups tenen models semblants en `accuracy`, però un detecta millor els casos que realment interessen a negoci.

La pregunta docent no és només quin número és més alt.

La pregunta és:

- quin error fa cada model?
- quin error és més costós?
- quina mètrica ho reflectix millor?

Ací és on `scikit-learn` ajuda no només a entrenar, sinó a estructurar la comparació.

## Pràctica guiada suggerida

1. feu una baseline simple
2. guardeu la mètrica principal
3. proveu un model alternatiu
4. compareu no només el resultat, sinó també el comportament dels errors

La conclusió final hauria de tindre una frase així:

`preferim este model perquè...`

Si l'alumnat no pot completar bé esta frase, encara no està comparant amb criteri suficient.

## Mini pràctica

Pregunta:

per què convé fer `train_test_split` abans d'entrenar?

## Solució orientativa

Perquè necessitem comprovar si el model generalitza sobre dades no vistes i no només si memoritza el conjunt d'entrenament.

## Resum final

`scikit-learn` és la via més clara per a ensenyar ML clàssic de manera ordenada i transferible a projectes reals.

El valor no està només en les llibreries que oferix, sinó en l'hàbit mental que imposa: preparar, separar, entrenar, avaluar i justificar.

## Com usar-la en estos projectes

- P1: baseline de classificació de tickets
- BiciTierra Market: comparativa de models i justificació
- P5: lectura predictiva simple abans d'escenaris més integrats

## Vegeu també

- `Python i Entorns`
- `Python per a Dades I`
- `Validació de models`
- `XAI amb SHAP i LIME`


## Per aprofundir

[Obri la píndola ampliada, amb pràctiques i exercicis](../PINDOLES_AMPLIADES/docs/scikit-learn-intro/index.md).
