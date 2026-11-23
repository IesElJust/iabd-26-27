---
title: MongoDB I Vector DB
---

# MongoDB I Vector DB

## No fan el mateix

`MongoDB` guarda documents, camps i estructures flexibles.

Una `vector DB` guarda representacions numeriques de fragments de text o altres objectes per a poder cercar per semblanca.

La confusió sol aparéixer perquè les dues poden guardar informació relacionada amb documents, però el paper que juguen és diferent.

## Com pensar MongoDB

`MongoDB` és una base de dades documental.

Cada registre sol ser un document JSON o semblant, amb camps descriptius.

Exemple de ticket:

```json
{
  "ticket_id": "T023",
  "canal": "web",
  "client_sector": "retail",
  "text_ticket": "Contrasenya canviada, pero continua dient invalid credentials",
  "departament_sospitat": "identitat",
  "estat": "obert"
}
```

Ací ens interessa:

- guardar l'objecte complet
- consultar per camps
- actualitzar l'estat
- filtrar per categoria, canal o urgència

## Com pensar una vector DB

Una `vector DB` no està pensada principalment per consultar per camps com `estat = obert`.

Està pensada per respondre preguntes del tipus:

- quin fragment s'assembla més a esta pregunta?
- quins textos són semànticament pròxims?

Exemple:

Si preguntem:

`"Quants intents fallits bloquegen el compte?"`

la vector DB pot recuperar el fragment del document de política de contrasenyes encara que la pregunta no repetisca exactament les mateixes paraules.

## Quan usar MongoDB

- tickets
- formularis
- documents amb metadades
- resultats de processos

## Quan MongoDB és suficient

Si el problema és principalment operatiu i estructurat, MongoDB pot ser suficient per si sola.

Per exemple:

- guardar tickets
- guardar formularis validats
- buscar per estat o data
- mantindre un historial de processos

## Quan usar vector DB

- fragments de manuals
- preguntes frequents
- politiques internes
- base per a `RAG`

## Quan la vector DB aporta valor real

Quan les preguntes són textuals i obertes.

No busquem un camp concret, sinó el significat més pròxim dins d'un corpus.

## Patró habitual al curs

1. MongoDB per a dades de negoci i metadades.
2. Vector DB per al corpus documental.
3. API per unir consulta, recuperacio i resposta.

## Exemple combinat

En un helpdesk:

- MongoDB guarda el ticket, el canal, el client i l'estat
- la vector DB guarda fragments del manual de VPN, del procediment de correu i de la política de contrasenyes
- l'API rep la pregunta, recupera fragments i genera resposta

## Exemple guiat de classe

Situació:

- un usuari obri un ticket perquè no pot entrar al correu
- l'equip vol guardar l'incident i, a més, donar una resposta assistida amb documentació interna

Pas 1:

Guardar en `MongoDB`:

- `ticket_id`
- `client`
- `text_ticket`
- `estat`
- `prioritat`

Pas 2:

Guardar en la `vector DB` fragments de:

- política de contrasenyes
- manual de correu
- procediment de recuperacio d'accés

Pas 3:

Quan arriba la pregunta, el sistema:

1. busca el context rellevant en la `vector DB`
2. usa eixe context per construir la resposta
3. actualitza en `MongoDB` l'estat del ticket si cal

Conclusió docent:

L'alumnat ha de veure que una tecnologia governa l'operativa i l'altra governa la recuperacio semàntica.

## Error habitual

Pensar que una vector DB substitueix una base de dades operativa completa.

També és un error guardar documents sense metadades mínimes. En un sistema real convé saber:

- d'on ix el fragment
- a quina política o manual pertany
- si és una versió vigent o antiga

## Mini practica

Classifica estos casos entre `MongoDB`, `vector DB` o `totes dues`:

1. Guardar l'estat actual d'un ticket.
2. Recuperar el fragment més rellevant d'un manual intern.
3. Mostrar a l'usuari els tickets oberts del departament de correu.
4. Donar suport a una resposta `RAG` sobre procediments interns.

## Solució orientativa

1. `MongoDB`
2. `vector DB`
3. `MongoDB`
4. `totes dues`

Explicació:

- `MongoDB` gestiona millor l'operativa i els camps estructurats.
- la `vector DB` resol la cerca semàntica.
- en `RAG`, normalment necessitem estructura operativa i recuperació documental.

## Segona mini practica

Tens estos dos objectius:

1. buscar tots els incidents de terminal `T2` amb severitat `high`
2. trobar el fragment de procediment més pròxim a la pregunta "què fer quan hi ha saturació de terminal?"

Pregunta:

Quina tecnologia encaixa millor en cada objectiu?

## Solució orientativa

1. `MongoDB` o una base orientada a dades estructurades
2. `vector DB`

Explicació:

- el primer cas és una consulta per camps concrets
- el segon és una consulta semàntica sobre text

## Resum final

`MongoDB` i una `vector DB` no competeixen necessàriament. Sovint es complementen: una governa dades de negoci i l'altra ajuda a recuperar coneixement textual.

## Com portar-ho a aula

- P1: fer que l'equip decidisca quins camps van a `MongoDB` i quins documents van a la `vector DB`
- P5: usar esta píndola per justificar una arquitectura amb capa operativa i capa documental
- criteri docent: si l'alumnat diu que tot va a una sola base sense distingir usos, encara no ha entes la decisio arquitectonica
