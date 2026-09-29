---
title: Validació De Models
---

# Validació De Models

## Idea clau

Un model no és bo perquè "funcione" amb les dades d'entrenament. Cal comprovar si generalitza.

Si un model memoritza massa el conjunt d'entrenament, pot donar resultats aparentment molt bons dins de classe però fallar quan rep dades noves. Validar és comprovar si allò que hem aprés serveix fora de les dades que ja coneixiem.

## Minims que sempre heu de fer

- separar `train` i `test`
- usar una mètrica coherent amb el problema
- comparar almenys un baseline amb una opció millorada

## Què és separar `train` i `test`

El conjunt `train` servix per aprendre.

El conjunt `test` servix per comprovar si el model generalitza.

Si barregem els dos papers, l'avaluació deixa de ser fiable.

## Baseline

Un `baseline` és una referència simple. Ens ajuda a respondre una pregunta bàsica:

"El model realment aporta valor o només sembla sofisticat?"

Per exemple:

- en classificació, un baseline podria ser la classe majoritària
- en regressió, una predicció fixa com la mitjana

Si el model no millora clarament el baseline, cal revisar el problema o les dades.

## Metriques habituals

- regressió: `MAE`, `RMSE`
- classificació: `accuracy`, `precision`, `recall`, `F1`

## Com triar mètrica

No hi ha una mètrica universal.

En classificació:

- `accuracy` pot servir si les classes estan equilibrades
- `precision` importa si no volem massa falsos positius
- `recall` importa si no volem deixar casos importants sense detectar
- `F1` combina `precision` i `recall`

En regressió:

- `MAE` és fàcil d'interpretar
- `RMSE` penalitza més els errors grans

## Sobreajust i infraajust

`Overfitting` o sobreajust:

- el model aprén massa bé les dades d'entrenament
- però falla amb dades noves

`Underfitting` o infraajust:

- el model és massa simple
- ni tan sols aprén correctament el patró principal

## Riscos habituals

- fuga d'informació
- sobreajust
- dades molt desbalancejades

## Fuga d'informació

Hi ha fuga d'informació quan el model rep, d'una forma o altra, informació que en la realitat no tindria disponible en el moment de predir.

Exemples:

- crear variables amb dades futures
- normalitzar amb tot el dataset abans de separar `train` i `test`
- usar camps que són quasi equivalents a la resposta

## Dades desbalancejades

Si una classe és molt més freqüent que una altra, el model pot donar una `accuracy` alta i encara així ser inútil.

Per exemple, si el 95% dels casos són normals, un model que sempre diga "normal" pot semblar bo, però no detectarà incidències.

## Cross-validation

Quan hi ha poques dades, convé usar `cross-validation` per a comprovar si el comportament del model és estable i no depén massa d'una única partició.

## Exemple guiat de classe

Situació:

en `Predicció Comercial`, un equip presenta un model amb molt bon resultat però només ensenya una execució i cap comparació amb baseline.

Que hauria de passar:

1. separar clarament entrenament i prova
2. construir una referència simple, encara que siga la mitjana o una regla bàsica
3. comparar el model nou contra eixa referència
4. mirar si el guany és real o només aparent

Conclusió docent:

si no hi ha baseline ni test separat, encara no hi ha evidència suficient per confiar en el model.

## Exemple de lectura de mètrica

Suposa estos resultats en regressió:

- baseline: `MAE = 14.8`
- model A: `MAE = 9.2`
- model B: `MAE = 9.0`

Lectura raonable:

- A i B milloren clarament la baseline
- la diferència entre A i B és menuda
- si B és molt més complex, potser A ja és prou bona opció

El millor model no és sempre el més sofisticat, sinó el que millora prou i es pot defensar amb criteri.

## Mini pràctica

- Agafa dos models.
- Compara els resultats sobre el mateix conjunt de test.
- Explica quin triaries i per que.

## Segona mini pràctica

Tens un problema de classificació amb classes desbalancejades.

Resultats:

- model 1: `accuracy = 0.95`, `recall` de la classe crítica = `0.20`
- model 2: `accuracy = 0.89`, `recall` de la classe crítica = `0.81`

Pregunta:

Quin model sembla més útil si el cost de no detectar la classe crítica és alt?

## Solució orientativa

El model 2 sembla més útil, perquè detecta molt millor la classe crítica encara que l'`accuracy` global siga menor.

La lectura important és esta:

- no totes les errades costen igual
- la mètrica correcta depén del risc del problema

## Resum final

Validar no és un tràmit. És el procés que separa una demo aparentment convincent d'una solució tècnica mínimament fiable.

## Com portar-ho a aula

- BiciTierra Market: exigir sempre baseline, mètrica coherent i lectura final dels errors
- P1: reaprofitar esta píndola quan es compare una regla simple contra una classificació més robusta
- P5: usar-la si hi ha part predictiva i cal justificar per què una alerta o risc és creïble


## Per aprofundir

[Obri la píndola ampliada, amb pràctiques i exercicis](../PINDOLES_AMPLIADES/docs/validacio-de-models/index.md).
