---
title: EDA I Qualitat De Dades
---

# EDA I Qualitat De Dades

## Què és l'EDA

`EDA` significa `Exploratory Data Analysis`. És l'anàlisi exploratòria inicial que fem abans de modelar.

L'objectiu no és fer gràfics per decorar, sinó entendre:

- què tenim
- què falta
- què està malament
- què pot explicar el problema de negoci

## Preguntes bàsiques

Abans de modelar convé respondre:

- quines variables hi ha?
- quin tipus de dades són?
- hi ha valors nuls?
- hi ha categories estranyes?
- hi ha valors extrems?
- hi ha duplicats?

## Qualitat de dades

La qualitat de dades no és només una qüestió tècnica. Si les dades estan malament, les decisions de negoci també poden estar-ho.

Problemes habituals:

- camps buits
- formats inconsistents
- duplicats
- categories mal escrites
- valors impossibles

## Exemple curt

Suposa un dataset de clients amb estos casos:

- un client amb `annual_spend` buit
- dues files amb perfils quasi iguals
- `returns_ratio` molt alt en un sol cas

L'EDA hauria de portar-vos a preguntar:

- és un error de captura o una dada real?
- cal imputar, eliminar o marcar el cas?
- eixe extrem és informatiu o és soroll?

## Exemple guiat de classe

Situació:

en `Predicció Comercial`, abans de modelar trobem:

- un client amb `annual_spend` buit
- valors de retorn molt diferents entre clients
- canals i ciutats amb comportaments desiguals

Ruta raonable:

1. detectar quins camps tenen nuls
2. localitzar si el problema és puntual o repetit
3. decidir si la dada es pot imputar, marcar o excloure
4. escriure l'impacte que tindria ignorar-ho

Conclusió docent:

una `EDA` bona no acaba en "ja hem mirat les dades", sinó en decisions explícites sobre què es considera fiable i què no.

## Mini pràctica

Observa este fragment:

```text
customer_id,annual_spend,orders_last_12m,returns_ratio
C018,,8,0.11
C020,3560,8,0.01
```

Pregunta:

Quins problemes detectes i quines decisions podries prendre abans de modelar?

## Solució orientativa

Problema principal:

- `annual_spend` està buit a `C018`

Possibles decisions:

- imputar si hi ha criteri raonable
- eliminar el cas si és residual i crític per al model
- mantenir-lo però crear una bandera de valor absent

La decisió correcta depén del context i del volum de dades, però el que no es pot fer és ignorar el problema.

## Segona mini practica

Tens estes dues files:

```text
C007,34,Oliva,ecommerce,3560,445,8,0.01,electric,medium
C020,34,Alzira,store,3560,445,8,0.01,electric,medium
```

Pregunta:

Per què val la pena revisar si hi ha duplicat funcional o si simplement hi ha dos perfils molt pareguts?

## Solució orientativa

Perquè si realment és un duplicat, pot distorsionar el model o la segmentació. Si no ho és, pot ser només una coincidència de perfil.

L'important és no assumir automàticament ni una cosa ni l'altra sense revisar més context.

## Resum final

Una bona `EDA` transforma un dataset desconegut en un conjunt de decisions conscients sobre qualitat, estructura i risc.

## Com portar-ho a aula

- BiciTierra Market: exigir que cada problema detectat acabe en una decisió escrita
- P1: reaprofitar la mateixa lògica per a soroll textual, quasi duplicats i categories confuses
- criteri docent: si hi ha gràfics o taules però no hi ha decisions, l'EDA encara és superficial


## Per aprofundir

[Obri la píndola ampliada, amb pràctiques i exercicis](../PINDOLES_AMPLIADES/docs/eda-i-qualitat-de-dades/index.md).
