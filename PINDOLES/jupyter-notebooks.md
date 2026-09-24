---
title: Jupyter Notebooks
---

# Jupyter Notebooks

## Per a què servixen

Un `Jupyter Notebook` és molt útil quan volem combinar en un mateix espai:

- explicació
- codi
- proves ràpides
- resultats
- gràfics

Dit d'una manera molt simple: un notebook és com una llibreta tècnica on podem contar què estem fent, executar-ho i veure el resultat sense eixir del mateix lloc.

Per això és tan útil quan encara estem pensant, provant o justificant decisions.

## Què veureu realment dins d'un notebook

Normalment hi ha dos tipus de cel·les:

- cel·les de text o `markdown`, on expliquem què volem fer
- cel·les de codi, on carreguem dades, fem càlculs o provem models

La idea bona no és alternar text i codi perquè quede bonic, sinó perquè qualsevol persona puga seguir el fil del treball.

En este curs són especialment útils per a:

- EDA
- neteja de dades
- proves de classificació
- validació de models
- experiments ràpids amb text o sèries temporals

## Quan és millor un notebook

- quan estem explorant
- quan volem justificar una decisió amb passos visibles
- quan encara no tenim una llibreria o aplicació tancada

## Quan no és el millor format

- quan ja tenim lògica estable i reusable
- quan el codi ha de passar a producció
- quan necessitem molta modularitat

Un error molt comú és pensar que, si un notebook ja funciona, ja és la solució final. No és així.

Un notebook sol ser un espai de prova, exploració o demostració. Si la lògica es torna estable, després convé passar-la a scripts, mòduls o aplicacions més netes.

## Bones pràctiques mínimes

- posar títols i subtítols clars
- separar exploració, transformació i conclusions
- no deixar cel·les trencades
- documentar què es vol demostrar amb cada bloc

## Estructura recomanada

1. objectiu del notebook
2. càrrega de dades
3. qualitat i EDA
4. tractament de dades
5. prova o model
6. conclusions

## Exemple guiat de classe

Situació:

en `Predicció Comercial`, volem saber si les vendes semblen dependre del canal, del descompte i de les sessions web.

Un notebook raonable podria tindre:

1. una cel·la que explique la pregunta de negoci
2. una cel·la que carregue `sales_history.csv`
3. una cel·la que revise nuls i tipus de dada
4. una cel·la que compare vendes per canal
5. una cel·la final amb una conclusió curta sobre què sembla important

El valor del notebook no és només el codi. És que permet veure el camí entre la pregunta inicial i la conclusió.

## Com saber si un notebook està ben fet

Si una altra persona l'obri, hauria de poder entendre:

- quina pregunta intenta respondre
- quines dades està usant
- què ha trobat
- i quina decisió o següent pas proposa

Si només veu codi solt i taules sense context, el notebook encara és feble.

## Error habitual

Convertir el notebook en una successió de proves sense fil conductor.

## Mini pràctica

Pregunta:

Si tens un notebook per a predicció comercial, quines dos seccions no haurien de faltar mai abans del modelatge?

## Solució orientativa

- una secció de càrrega i comprensió de dades
- una secció de qualitat/EDA abans de modelar

## Resum final

El notebook és una eina de pensament visible. Té molt valor si ajuda a entendre el camí que porta a una decisió tècnica.

## Com usar-lo en estos projectes

- P1: explorar tickets i provar una baseline abans del `RAG`
- BiciTierra Market: separar EDA, modelatge i segmentació amb conclusions curtes al final de cada bloc
- P3: validar rangs i alertes abans de desplegar massa infraestructura
- P4: comprovar regles de validació sobre la cua d'entrada abans d'automatitzar
- P5: provar una lectura de risc o una analítica puntual abans de la integració global

## Criteri docent rapid

Si el professorat pot llegir el notebook de dalt a baix i entendre el problema, la prova i la conclusió sense haver d'endevinar el fil, el notebook ja està fent bé la seua funció.
