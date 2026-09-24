---
title: Clustering I Segmentació
---

# Clustering I Segmentació

## Idea clau

Segmentar és agrupar casos semblants quan no tenim una etiqueta prèvia.

En negoci, això és útil per descobrir perfils de clients, patrons d'ús o comportaments semblants.

## No és màgia

Un algoritme de `clustering` no "descobreix la veritat". El que fa és agrupar segons la representació de les dades que li donem.

Per això el resultat depén de:

- les variables triades
- l'escalat
- l'algoritme
- els paràmetres

## Dos casos coneguts

### K-Means

Agrupa al voltant de centres.

És útil quan esperem grups relativament compactes.

### DBSCAN

Agrupa per densitat.

És útil quan hi ha soroll o quan no volem forçar tots els punts a pertànyer a un clúster.

## Error habitual

Pensar que el nombre de grups ix automàticament "bé" sense justificació.

## Exemple conceptual

Si segmentem clients amb:

- `annual_spend`
- `avg_order_value`
- `orders_last_12m`

podem trobar perfils com:

- clients ocasionals de baix valor
- clients freqüents de valor mitjà
- clients premium amb despesa alta

## Exemple guiat de classe

Situació:

en `Predicció Comercial`, l'equip vol segmentar clients per a decidir campanyes i priorització comercial.

Variables inicials raonables:

- `annual_spend`
- `avg_order_value`
- `orders_last_12m`
- `returns_ratio`

Que cal fer abans de l'algorisme:

1. revisar si hi ha nuls o casos estranys
2. decidir quines variables expliquen millor el valor del client
3. pensar quins perfils comercials esperaríem trobar

Que cal fer després:

1. mirar si els grups tenen sentit llegible
2. posar-los nom de negoci, no només número de clúster
3. decidir quina acció comercial faria cada equip amb cada segment

Conclusió docent:

si el grup no es pot interpretar ni convertir en decisió, la segmentació encara no està ben tancada.

## Mini pràctica

Tens tres clients:

- A: `annual_spend=720`, `orders=7`
- B: `annual_spend=3560`, `orders=8`
- C: `annual_spend=4020`, `orders=8`

Pregunta:

Quin perfil sembla més pròxim a un segment premium? Quin podria quedar separat del grup de més valor?

## Solució orientativa

- `B` i `C` semblen candidats a segments d'alt valor
- `C` encara més, perquè la despesa és superior
- `A` quedaria previsiblement en un segment de valor baix o ocasional

## Resum final

El `clustering` és útil quan ajuda a construir una lectura accionable del negoci, no quan només genera grups difícils d'interpretar.

## Com portar-ho a aula

- BiciTierra Market: fer escriure primer segments esperats i després comparar-los amb el resultat real
- criteri docent: el segment ha d'acabar en una acció, una recomanació o una prioritat comercial
