---
title: RAG I Embeddings
---

# RAG I Embeddings

## Idea clau

Un `LLM` no coneix necessàriament els documents interns d'una empresa. El patró `RAG` recupera fragments rellevants abans de generar la resposta.

Un model generatiu pot escriure text amb molta fluïdesa, però això no significa que conega la documentació concreta d'una empresa, ni que la tinga actualitzada. Si li preguntem sense donar-li context, és molt probable que improvise una resposta plausible. `RAG` intenta reduir eixe problema fent un pas previ de recuperació d'informació.

Dit d'una manera més simple: `RAG` és una forma d'evitar que el model responga "de memòria" quan en realitat necessita llegir abans uns documents.

## Què intenta resoldre exactament

Un `LLM` per si sol pot ser molt bo redactant, resumint o reformulant. El problema apareix quan necessitem que parle sobre:

- manuals interns
- polítiques d'empresa
- procediments que canvien
- documentació que no forma part del seu entrenament

Sense una capa de recuperació, el model pot fer tres coses perilloses:

- inventar una resposta plausible
- barrejar coneixement general amb coneixement que no toca
- sonar segur encara que no tinga base suficient

Per això `RAG` no és només una millora tècnica. És una forma de posar el model a treballar amb evidència concreta.

## Què és un embedding

Un `embedding` és una representació numèrica d'un text. La idea és convertir frases o fragments en vectors, de manera que textos amb significat semblant queden prop en l'espai vectorial.

Per exemple:

- "No puc entrar al portal"
- "No em deixa iniciar sessió"

tenen paraules diferents, però poden acabar amb vectors semblants perquè parlen d'un problema pròxim.

Gràcies a això podem fer cerca semàntica, no només cerca per paraules exactes.

La idea important per a principiants és esta: el sistema no compara textos com una persona que llig paraula a paraula, sinó com a punts en un espai matemàtic on allò semblant queda "més prop".

No cal entendre tota la matemàtica per aprofitar el concepte. El que cal entendre és el seu efecte pràctic: podem recuperar textos rellevants encara que la pregunta no use exactament les mateixes paraules que el document.

## Peces del patro

1. Documents
2. Trossejat o `chunking`
3. Embeddings
4. Index o vector DB
5. Recuperacio
6. Generacio de resposta

## Com funciona el flux complet

1. Es reuneix el corpus documental.
2. Els documents es netegen i es divideixen en fragments manejables.
3. Cada fragment es transforma en embedding.
4. Els embeddings es guarden en un índex o vector DB.
5. L'usuari fa una pregunta.
6. La pregunta també es transforma en embedding.
7. Es busquen els fragments més pròxims.
8. Eixos fragments s'envien al `LLM` com a context.
9. El model genera una resposta basada en eixe context.

## On està realment la dificultat

Moltes vegades sembla que el pas important és només "cridar el model". Però en `RAG` la part més delicada sol estar abans:

- quins documents entren al corpus
- com es netegen
- com es parteixen
- quins fragments es recuperen
- com decidim si el context és suficient o no

Si això falla, el model pot redactar molt bé una resposta mal fonamentada.

## Per què no val qualsevol fragmentació

Si fem fragments massa grans:

- es barreja massa informació
- es recuperen trossos poc precisos
- augmenta el soroll

Si fem fragments massa menuts:

- es perd context
- es trenquen procediments o idees completes

Per això el `chunking` és una decisió important. No és només una qüestió tècnica; afecta directament la qualitat de la resposta.

## Exemple teòric curt sobre `chunking`

Suposa un procediment amb estos passos:

1. comprovar intents fallits
2. revisar si hi ha bloqueig temporal
3. validar identitat per correu corporatiu
4. aplicar desbloqueig urgent

Si partim el text massa malament, podem acabar amb un fragment que només diga:

`aplicar desbloqueig urgent`

Sense el context anterior, el model podria donar a entendre que el desbloqueig urgent sempre s'ha d'aplicar, quan en realitat depén d'una validació prèvia.

La lliçó és clara: un bon fragment no és només curt; ha de conservar una unitat de sentit.

## Quan te sentit

- documentació interna
- FAQ d'empresa
- manuals, procediments i politiques

També és útil quan els documents canvien sovint i no volem reentrenar un model cada vegada que es modifica una política o un manual.

## Quan no te sentit per si sol

- dades estructurades que demanen calcul
- processos que requereixen permisos i accions
- casos on cal validació humana estricta

Per exemple, si la pregunta és "quantes incidències hi ha obertes hui?", això no s'hauria de resoldre només amb `RAG`, perquè no és un problema documental sinó una consulta sobre dades actuals.

## Diferencia entre cercador i RAG

Un cercador et torna documents o fragments.

Un sistema `RAG`:

- recupera fragments
- els passa al model
- genera una resposta redactada

Això és útil, però també més perillós, perquè la part generativa pot inventar o resumir malament si el context és pobre.

## Diferencia entre pregunta documental i pregunta de dades

Una part clau per a l'alumnat és aprendre a distingir estos dos casos:

Cas documental:

- "què diu el protocol quan un compte queda bloquejat?"

Cas de dada actual:

- "quants comptes bloquejats hi ha ara mateix?"

El primer és bon candidat per a `RAG`.

El segon necessita una consulta sobre dades actuals, no només documents.

Si no distingim açò, l'alumnat pot intentar resoldre-ho tot amb `RAG` i això genera solucions poc fiables.

## Errors habituals

- chunks massa grans
- documents mal nets
- no citar o no conservar traçabilitat
- respondre encara que no hi haja context suficient

També són errors habituals:

- posar documents duplicats al corpus
- no filtrar versions antigues
- no distingir entre document vigent i document històric
- recuperar molts fragments irrelevants i saturar el model

## Bon criteri de qualitat

Un bon sistema `RAG` no és el que sempre respon. És el que:

- recupera context útil
- respon de forma ajustada
- mostra d'on ix la informació
- i sap dir "no tinc prou context" quan toca

## Exemple guiat de classe ampliat

Situació:

en `Helpdesk`, l'usuari pregunta: `No puc entrar i posa user blocked. Què he de fer?`

El sistema recupera dos fragments:

1. `El bloqueig temporal per 5 intents fallits dura 15 minuts.`
2. `El desbloqueig urgent requereix verificació per correu corporatiu.`

Una resposta correcta no hauria de:

- dir que el compte està definitivament desbloquejat
- inventar un tercer procediment que no apareix als documents
- prometre una acció automàtica que el sistema no fa

Una resposta bona sí que hauria de:

- explicar el bloqueig temporal
- explicar la condició del desbloqueig urgent
- deixar clar que està parlant segons el context recuperat

Conclusió docent:

el valor del `RAG` no és que parle molt bé, sinó que parle bé a partir de proves documentals.

## Mini pràctica

- Agafa 3 documents interns.
- Trosseja'ls en fragments curts.
- Escriu quines preguntes podria respondre el sistema i quines no.

## Solució orientativa de la mini pràctica

Exemple:

Si els documents tracten sobre:

- política de contrasenyes
- manual de VPN
- procediment de correu

el sistema podria respondre preguntes com:

- quants intents fallits bloquegen el compte?
- què cal revisar abans d'escalar una incidència de correu?
- què s'ha de comprovar si la VPN dona error de certificat?

I no hauria de respondre per si sol preguntes com:

- quants tickets hi ha oberts hui?
- quin usuari concret va fallar més logins esta setmana?
- pots desbloquejar-me el compte ara mateix?

La raó és que aquestes últimes demanen dades actuals o accions operatives, no només coneixement documental.

## Pràctica guiada llarga

### Objectiu

Entendre tot el recorregut d'un sistema `RAG` menut: corpus, fragments, pregunta, recuperació i resposta.

### Situació

Imagina que l'equip de `Helpdesk` vol donar suport a consultes sobre:

- política de contrasenyes
- manual de VPN
- procediment de correu corporatiu

L'objectiu no és crear un assistent perfecte, sinó aprendre a distingir què pot respondre bé i què no.

### Pas 1. Delimitar el corpus

Abans de res, cal decidir quins documents entren.

Preguntes que s'han de respondre:

- els documents són vigents?
- hi ha duplicats o versions antigues?
- tots parlen realment del problema que volem resoldre?

Si el corpus és confús, el sistema ja naix confús.

### Pas 2. Pensar els fragments

Ara cal decidir com partiríeu els documents.

No es tracta de tallar per tallar. La pregunta correcta és:

- cada fragment conserva una idea completa?
- un procediment queda sencer o queda trencat?

Exercici:

agafa un procediment de 6 o 7 línies i intenta dividir-lo en 2 o 3 fragments. Després pregunta't si cada tros es podria entendre per separat.

### Pas 3. Definir preguntes bones i preguntes roïnes per a `RAG`

Preguntes bones:

- què diu la política quan hi ha 5 intents fallits?
- què s'ha de comprovar si la VPN dona error de certificat?

Preguntes roïnes per a `RAG` si va sol:

- quants tickets hi ha oberts ara mateix?
- pots desbloquejar-me el compte ara?

Ací l'alumnat ha d'aprendre que una cosa és consulta documental i una altra cosa és dada actual o acció operativa.

### Pas 4. Simular la recuperació

Sense necessitat de muntar tota la infraestructura, feu la prova a mà:

1. escriviu una pregunta
2. decidiu quins 2 fragments serien els més útils
3. expliqueu per què

Exemple:

Pregunta:

`Què passa si em bloquegen el compte?`

Fragments recuperats:

1. `El bloqueig temporal per 5 intents fallits dura 15 minuts.`
2. `El desbloqueig urgent requereix verificació per correu corporatiu.`

### Pas 5. Escriure una resposta acceptable

Ara redacteu una resposta que:

- use només eixos fragments
- no invente passos nous
- deixe clar si falta context

Resposta orientativa:

`Si el compte queda bloquejat després de 5 intents fallits, el bloqueig temporal dura 15 minuts. Si cal un desbloqueig urgent, s'ha de fer amb verificació per correu corporatiu.`

### Pas 6. Tancar límits del sistema

Per acabar, escriviu tres coses:

- una pregunta que el sistema sí hauria de respondre
- una pregunta que hauria de rebutjar per falta de context
- una pregunta que en realitat exigix dades actuals o una altra capa del sistema

### Què hauria d'aprendre l'alumnat

- que `RAG` no és "posar documents a un model"
- que el corpus i el `chunking` condicionen molt el resultat
- que no tot el que sona a consulta s'ha de resoldre amb recuperació documental

### Criteri docent

Si l'alumnat sap distingir entre resposta documental, consulta de dades i acció operativa, ja està entenent la peça important del patró.

## Segona mini pràctica

Suposa que has recuperat estos dos fragments:

1. "El bloqueig temporal per 5 intents fallits dura 15 minuts."
2. "El desbloqueig urgent requereix verificació per correu corporatiu."

Pregunta:

Quina seria una resposta acceptable a "què passa si em bloquegen el compte?"

## Solució orientativa

Una resposta acceptable seria:

"Si el compte queda bloquejat després de 5 intents fallits, el bloqueig temporal dura 15 minuts. Si cal un desbloqueig urgent, s'ha de fer amb verificació per correu corporatiu."

És bona resposta perquè:

- usa el context recuperat
- no inventa passos nous
- respon de forma directa

## Resum final

`RAG` no substitueix el coneixement de domini, la neteja documental ni el criteri funcional. És un patró molt útil, però només funciona bé quan el corpus està cuidat i quan el sistema controla els seus límits.

## Com portar-ho a aula

- P1: fer separar clarament què resol el corpus documental i què resol la part operativa del ticket
- P5: usar-lo només quan hi haja una necessitat real de consulta sobre documentació interna
- criteri docent: si l'alumnat intenta usar `RAG` per a preguntes que en realitat són consultes de dades o accions, encara no ha entés bé el patró
