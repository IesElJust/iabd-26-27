---
title: MLflow Introductori
---

# MLflow Introductori

## Per a què servix

Quan comparem models, és molt fàcil perdre el fil de:

- quin dataset hem usat
- quins paràmetres tenia cada prova
- quina mètrica ha donat millor resultat

`MLflow` és una eina de seguiment d'experiments.

Per a algú que comença, es pot entendre així: `MLflow` és una manera ordenada de no perdre el rastre del que has provat.

No cal pensar-lo com una plataforma enorme. En este curs, el primer valor és molt simple: saber què has comparat i per què has triat una prova i no una altra.

## Què registra

- nom de l'experiment
- paràmetres
- mètriques
- artefactes com gràfics o models guardats

En la pràctica això significa que, quan tornes l'endemà, no has de confiar en la memòria per recordar quina prova era millor.

## Per què és útil al curs

No cal usar-lo com una eina avançada de producció per traure profit. Ja ajuda molt si servix per comparar proves de manera ordenada.

## Exemple guiat de classe

Situació:

en `Predicció Comercial`, un equip prova dos models i tres configuracions, però al cap de dos dies ja no recorda quina combinació va donar millor resultat.

Sense seguiment, solen passar coses com:

- no saber quin dataset exacte s'ha usat
- confondre mètriques de proves diferents
- repetir experiments perquè no han quedat registrats

Amb una eina com `MLflow`, o amb una disciplina semblant encara que siga manual, l'equip hauria de guardar:

- nom de la prova
- model utilitzat
- paràmetres principals
- mètrica obtinguda
- comentari curt sobre què s'ha provat

Conclusió docent:

el valor no és només tècnic; és fer que els experiments siguen comparables i defensables.

## Exemple conceptual

Prova A:

- model: `RandomForest`
- `max_depth = 5`
- `F1 = 0.74`

Prova B:

- model: `RandomForest`
- `max_depth = 10`
- `F1 = 0.79`

Sense seguiment, és fàcil oblidar quina combinació exacta ha donat millor resultat.

## Què passa si no ho registrem

Sense una disciplina d'experiments, és molt habitual:

- repetir proves ja fetes
- no poder justificar una elecció davant del professorat
- confondre una mètrica d'una prova amb una altra
- ensenyar el "millor model" sense saber reproduir-lo

Per això, encara que l'eina siga nova, la idea de fons és molt senzilla: cada prova important ha de quedar identificada.

## Exemple molt simple de pensament experimental

Suposa que proves:

- una baseline simple
- un arbre amb profunditat xicoteta
- un arbre amb profunditat gran

El que vols poder contestar després és:

- quina prova era cada una
- amb quines dades es va fer
- quina mètrica va donar
- quina triaries i per què

`MLflow` ajuda exactament a això.

## Error habitual

Comparar models i després no saber reproduir la millor prova.

## Mini pràctica

Pregunta:

Quines dades mínimes voldries guardar si compares dos models per predir vendes?

## Solució orientativa

Com a mínim:

- nom del model
- paràmetres principals
- mètrica triada
- versió o descripció del dataset

## Resum final

`MLflow` ajuda a convertir proves disperses en experiments comparables i reproduïbles.

## Com portar-ho a aula

- BiciTierra Market: usar-lo com a hàbit de registre d'experiments encara que siga en nivell introductori
- P5: usar-lo si hi ha part predictiva amb diverses iteracions o models
- criteri docent: si l'equip no pot explicar quina prova concreta està ensenyant, el treball experimental encara és feble

## Criteri docent ampliat

Si un equip diu "este model és millor" però no pot dir quina execució, amb quins paràmetres i sobre quin dataset, encara no ha tancat bé la part experimental.


## Per aprofundir

[Obri la píndola ampliada, amb pràctiques i exercicis](../PINDOLES_AMPLIADES/docs/mlflow-intro/index.md).
