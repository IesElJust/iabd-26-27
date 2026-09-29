---
title: XAI Amb SHAP I LIME
---

# XAI Amb SHAP I LIME

## Per que importa

No n'hi ha prou amb dir que un model encerta. Cal poder explicar, almenys de forma aproximada, per quines variables ha pres una decisio.

En entorns empresarials, una predicció sense explicació genera dos problemes:

- costa confiar en el model
- costa detectar si s'esta equivocant per una raó rellevant

Per això la `XAI` no és només un extra acadèmic. És una ajuda per llegir el comportament del model i discutir-lo amb criteri.

Per a qui comença, la idea central és esta: una predicció sola diu "què ha passat"; una explicació intenta dir "per què sembla que ha passat".

No és exactament una finestra perfecta a l'interior del model, però sí una pista molt útil per revisar si el comportament sembla coherent.

## Què busquem

- entendre quines variables pesen mes
- detectar patrons sospitosos
- justificar decisions davant direcció o client

En altres paraules, no volem només veure una gràfica bonica. Volem poder discutir si el model està basant-se en factors que tenen sentit.

## Explicació global i explicació local

No totes les explicacions responen la mateixa pregunta.

Esta diferència és molt important perquè l'alumnat sovint confon les dues coses.

Una explicació global parla del model en general.

Una explicació local parla d'un cas concret.

Si no distingim això, podem extraure conclusions errònies a partir d'una sola predicció o, al revés, voler justificar un cas concret només amb una importància general de variables.

### Explicacio global

Intenta respondre:

"En general, quines variables són més importants en este model?"

Exemple:

- en un model de vendes, poden pesar molt `marketing_spend`, `avg_discount` i `website_sessions`

### Explicacio local

Intenta respondre:

"Per què este cas concret ha rebut esta predicció?"

Exemple:

- un client concret queda en un segment premium perquè té `annual_spend` alt, `returns_ratio` baix i `orders_last_12m` elevat

## Dos enfocaments coneguts

- `LIME`: explica prediccions locals aproximant el comportament del model.
- `SHAP`: reparteix contribucions de les variables a una predicció.

## Com entendre LIME

`LIME` mira un cas concret i construeix una aproximació simple del model al seu voltant.

La idea no és descriure tot el model, sinó explicar aquella predicció concreta.

És útil quan volem entendre per què el model ha classificat un client, un ticket o una incidència d'una determinada manera.

## Com entendre SHAP

`SHAP` reparteix la predicció entre les variables d'entrada, com si cada variable aportara una part del resultat final.

En la pràctica, això permet dir coses com:

- esta venda es prediu alta perquè hi ha molt trànsit web i descompte moderat
- esta incidència es considera greu per la cua elevada i la baixa disponibilitat de grues

La utilitat didàctica és que obliga a traduir el model a llenguatge llegible.

No n'hi ha prou amb dir "la gràfica mostra importàncies". Cal poder dir:

- quina variable empeny cap amunt
- quina frena la predicció
- si això encaixa amb el negoci o amb l'operació

## Exemples conceptuals

Suposa un model que prediu vendes mensuals.

Una predicció concreta podria ser `71 unitats`.

Lectura tipus `SHAP`:

- `website_sessions` aporta `+9`
- `marketing_spend` aporta `+6`
- `stock_units` aporta `-3`
- `avg_discount` aporta `+2`

No vol dir que el model "fa exactament eixa suma" de forma humana, però sí que ens dona una lectura útil de cap a on empeny cada variable.

## Aplicacio al curs

- predicció comercial
- classificació de tickets
- projecte integrador final

## Exemple guiat de classe

Situació:

en `Predicció Comercial`, dos equips tenen models pareguts en mètrica, però només un sap explicar per què prediu millor vendes altes.

Lectura possible amb `SHAP`:

- `website_sessions` empeny cap amunt
- `marketing_spend` empeny cap amunt
- `stock_units` limita la predicció

Que ha de fer l'alumnat:

1. mirar si les variables importants tenen sentit de negoci
2. detectar si n'hi ha alguna sospitosa o sorprenent
3. escriure una conclusió curta: "el model sembla confiar sobretot en..."

Conclusió docent:

no volem que memoritzen la llibreria, sinó que sàpien llegir si el model està raonant de forma creïble.

## Què ens ajuda a detectar

- variables que aparentment no haurien de pesar tant
- patrons possibles de biaix
- comportaments incoherents amb el negoci
- diferències entre allò que esperàvem i allò que realment usa el model

## Exemple teòric curt de lectura incorrecta i correcta

Lectura incorrecta:

- `website_sessions` és la variable més important, per tant sempre explica totes les vendes

Per què és incorrecta:

- una importància global no explica necessàriament tots els casos

Lectura més correcta:

- `website_sessions` sembla ser una de les variables que més pes tenen en general, però cal mirar també casos concrets per veure com actua junt amb altres factors

Esta diferència pareix menuda, però és clau per no simplificar massa el model.

## Error habitual

Pensar que si una eina d'`XAI` pinta un gràfic bonic, ja hem entés el model.

Cal interpretar l'explicació dins del context del problema.

## Mini pràctica

Imaginem un model de segmentació o classificació de clients amb estes variables:

- `annual_spend`
- `orders_last_12m`
- `returns_ratio`

Cas concret:

- `annual_spend = 4020`
- `orders_last_12m = 8`
- `returns_ratio = 0.00`

Pregunta:

Quines variables esperaríeu que empenyeren el model cap a un segment de client d'alt valor?

## Solució orientativa

- `annual_spend` alt: hauria d'empényer clarament cap a valor alt
- `orders_last_12m` elevat: reforça la idea de client actiu
- `returns_ratio` nul: ajuda positivament perquè no hi ha senyal de comportament problemàtic

Conclusió:

Si una explicació real mostrara que `returns_ratio` és quasi l'únic factor rellevant i `annual_spend` pesa poc, caldria revisar el model o les dades.

## Pràctica guiada llarga

### Objectiu

Aprendre a llegir una explicació de model sense confondre visualització amb comprensió real.

### Situació

En `Predicció Comercial`, dos equips tenen models amb mètriques paregudes. Ara cal decidir quin model és més creïble per presentar-lo a direcció.

### Pas 1. Començar per la pregunta correcta

Abans de mirar cap gràfica, cal preguntar:

- què intenta predir el model?
- quines variables esperaríem que influïren?
- hi ha factors que serien sospitosos si pesaren massa?

Per exemple, si predim vendes, seria lògic esperar pes en:

- `website_sessions`
- `marketing_spend`
- `stock_units`
- `avg_discount`

### Pas 2. Distingir lectura global i local

Ara feu esta separació:

- lectura global: quines variables pesen més en general?
- lectura local: per què este cas concret ha rebut esta predicció?

L'alumnat ha de practicar les dues coses per separat.

### Pas 3. Simular una lectura global

Suposeu que una eixida global diu:

- `website_sessions` pesa molt
- `marketing_spend` pesa prou
- `stock_units` pesa de manera moderada

Preguntes:

- això sembla coherent amb el negoci?
- hi ha alguna variable que sorprén massa?
- falta alguna variable que esperàveu important?

### Pas 4. Simular una lectura local

Ara suposeu un cas concret amb predicció alta.

Lectura local:

- `website_sessions` empeny cap amunt
- `marketing_spend` empeny cap amunt
- `stock_units` frena una mica

L'alumnat hauria d'escriure una frase com esta:

`La predicció és alta sobretot perquè hi ha molt trànsit i inversió comercial, tot i que l'estoc limita una part del potencial.`

### Pas 5. Detectar lectura roïna

Ara feu l'exercici contrari.

Si el model mostra que la variable més important és una que no té gaire sentit de negoci, com per exemple un identificador o un camp sospitós, què podria estar passant?

Possibles respostes:

- dades mal preparades
- fuga d'informació
- model que està aprofitant un patró accidental

### Pas 6. Tancar amb una conclusió defensable

L'alumnat hauria d'acabar escrivint:

- una conclusió global sobre el model
- una lectura d'un cas concret
- un dubte o risc que convindria revisar

### Què hauria d'aprendre l'alumnat

- que `XAI` no és decorar el model amb una gràfica
- que una explicació servix per discutir credibilitat
- que cal passar de la visualització al llenguatge de negoci o d'operació

### Criteri docent

Si l'alumnat pot traduir una eixida tipus `SHAP` o `LIME` a una explicació verbal creïble, està fent el pas important.

## Risc

Confondre "explicació aproximada" amb "prova absoluta" del funcionament intern.

També és un risc pensar que `XAI` arregla un model roí. No ho fa.

Si les dades estan mal, si hi ha fuga d'informació o si el model està mal plantejat, l'explicació pot continuar existint, però no convertirà màgicament la solució en fiable.

## Resum final

`XAI` no elimina la complexitat del model, però la fa discutible. Ens permet passar de "el model diu això" a "el model diu això per estes raons aproximades, i ara podem valorar si tenen sentit".

## Com portar-ho a aula

- BiciTierra Market: demanar sempre una lectura en llenguatge de negoci, no només la gràfica
- P5: usar-la per a discutir si un indicador de risc té sentit operatiu
- criteri docent: si l'alumnat no sap passar de la visualització a una explicació verbal defensable, encara no ha interioritzat la píndola

## Com portar-ho a aula

- BiciTierra Market: exigir almenys una explicació global i una lectura curta d'un cas concret
- P5: usar `XAI` per a justificar indicadors de risc o colls de botella
- criteri docent: si l'alumnat només ensenya la gràfica i no l'interpreta en llenguatge de negoci, la píndola no està ben aprofitada


## Per aprofundir

[Obri la píndola ampliada, amb pràctiques i exercicis](../PINDOLES_AMPLIADES/docs/xai-shap-lime/index.md).
