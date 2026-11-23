---
title: APIs REST
---

# APIs REST

## Per a que servixen

Permeten exposar funcionalitats d'un sistema a altres aplicacions.

Quan una aplicació envia una petició a una altra per Internet o dins d'una xarxa interna, normalment necessita una forma clara de demanar dades o executar una acció. Una `API REST` és una manera molt comuna d'organitzar eixes comunicacions.

Per a qui comença, es pot entendre així: una `API REST` és la porta ordenada per la qual altres programes poden parlar amb el teu sistema.

No venen a mirar el teu codi per dins. Només saben quina petició poden fer, quines dades han d'enviar i quina resposta poden esperar.

## Què és una API

Una `API` és una interfície. En el context web, és el contracte que diu:

- quines rutes existixen
- quines dades s'han d'enviar
- què tornarà el servidor
- què passa si alguna cosa falla

Per això una API es pareix molt més a un contracte que a una funció interna.

Una funció interna la controles tu completament. Una API l'han d'entendre i usar també altres peces del sistema.

## Idea de recurs

En `REST`, solem pensar en recursos:

- `tickets`
- `sensors`
- `clients`
- `prediccions`

Un recurs no és exactament una pantalla, sinó una entitat o servei amb el qual volem interactuar.

Esta idea costa al principi perquè moltes persones pensen en pantalles. En `REST` convé pensar en coses del sistema:

- tickets
- sensors
- clients
- prediccions

Després decidim quines operacions volem fer sobre eixes coses.

## Elements mínims

- recurs
- metodes `GET`, `POST`, `PUT`, `DELETE`
- entrada i eixida en JSON
- codis d'estat

## Significat habitual dels mètodes

- `GET`: obtindre informació
- `POST`: crear o llançar una operació
- `PUT`: reemplaçar o actualitzar completament
- `DELETE`: eliminar

No és obligatori usar-los sempre tots, però sí convé mantindre una lògica consistent.

La consistència és clau perquè fa que una altra persona puga intuir el comportament de l'API sense haver de preguntar-ho tot cada vegada.

## Exemple simple

Suposa una API per classificar tickets:

- `POST /tickets/classify`
- cos de petició: text del ticket
- resposta: categoria, prioritat i confiança

La idea és que qualsevol client puga enviar el text i rebre una resposta estructurada.

Esta paraula és important: `estructurada`.

No volem només un text lliure si després una altra aplicació l'ha de processar. Volem camps clars que es puguen llegir sense ambiguïtat.

Resposta possible:

```json
{
  "categoria": "identitat",
  "prioritat": "alta",
  "confidence": 0.87
}
```

## Per què JSON

`JSON` és fàcil de llegir per humans i màquines. Permet intercanviar dades estructurades com text, números, booleans, llistes i objectes.

Exemple:

```json
{
  "ticket": "No puc entrar al portal",
  "channel": "web"
}
```

## Codis d'estat

Els codis d'estat ajuden a entendre el resultat sense haver de llegir tota la resposta:

- `200`: tot correcte
- `201`: creat correctament
- `400`: petició mal formada
- `404`: recurs no trobat
- `500`: error intern del servidor

És important que l'alumnat no use sempre `200` encara que hi haja error funcional.

La raó és simple: el client no hauria d'haver de "deduir" l'èxit o el fracàs només llegint el cos de la resposta. El codi d'estat ja ha de donar una pista clara.

## Exemple de casos dins del curs

- enviar un ticket per classificar
- consultar sensors
- executar una predicció
- llançar un workflow

## Bones practiques basiques

- usar noms clars i estables
- separar dades d'entrada i d'eixida
- documentar què espera cada endpoint
- controlar errors previsibles
- provar tant casos correctes com incorrectes

## Exemple guiat de classe

Situació:

en `ClinicFlow`, una aplicació vol enviar una sol·licitud d'entrada i rebre el resultat de la validació.

Una API poc clara faria coses com:

- acceptar qualsevol cos de petició sense dir què falta
- tornar sempre `200`
- respondre amb textos lliures difícils de processar

Una API més útil faria:

- una ruta clara, com `POST /intake/validate`
- una entrada definida
- una resposta estructurada amb resultat i motiu
- un `400` si falten camps essencials

Conclusió docent:

una API bona no és la que només funciona, sinó la que es deixa usar bé des de fora.

## Exemple de cas correcte i incorrecte

### Cas correcte

Petició:

```json
{
  "ticket": "No puc entrar al portal",
  "channel": "web"
}
```

Resposta:

```json
{
  "categoria": "identitat",
  "prioritat": "alta"
}
```

### Cas incorrecte

Petició:

```json
{
  "channel": "web"
}
```

Resposta esperable:

```json
{
  "error": "Falta el camp ticket"
}
```

amb codi d'estat `400`.

## Bones pràctiques mínimes

- noms consistents
- errors clars
- separar dades d'entrada i d'eixida
- provar amb casos valids i fallits

## Error habitual

Confondre una API amb una simple funció local. Una API ha de pensar-se com un contracte que altres persones o serveis utilitzaran sense mirar el teu codi intern.

També és habitual:

- barrejar massa coses en una sola ruta
- no definir bé què s'espera d'entrada
- no controlar errors previsibles
- tornar respostes inconsistents segons el cas

## Mini pràctica

Vols exposar una funcionalitat per validar una sol·licitud clínica.

Pregunta:

Quin endpoint i quin mètode serien raonables per enviar una sol·licitud i rebre el resultat de la validació?

## Solució orientativa

Una opció defensable seria:

- `POST /intake/validate`

Per què?

- estem enviant dades al servidor
- volem executar una operació de validació
- el resultat és una resposta estructurada, no una simple lectura d'un recurs ja existent

## Pràctica guiada llarga

### Objectiu

Aprendre a dissenyar una API senzilla però coherent, pensada perquè una altra peça del sistema la puga entendre i usar sense mirar el codi intern.

### Situació

En `ClinicFlow`, una aplicació necessita enviar una sol.licitud d'entrada i rebre el resultat de la validació.

L'equip vol que la API servisca per a:

- rebre dades d'un formulari
- comprovar si falten camps crítics
- retornar un resultat estructurat
- indicar amb claredat si la petició és vàlida o no

### Pas 1. Definir què voleu exposar

Abans de pensar en codi o en framework, cal escriure què fa exactament l'endpoint.

En este cas:

- rep una sol.licitud clínica
- la valida
- torna el resultat de la validació

Esta descripció pareix simple, però ajuda a no barrejar massa responsabilitats dins de la mateixa ruta.

### Pas 2. Triar ruta i mètode

Ara decidiu:

- quin recurs o operació exposeu
- si és `GET`, `POST`, `PUT` o un altre mètode

En este cas, una opció raonable és:

- `POST /intake/validate`

Per què?

- enviem dades al servidor
- executem una operació
- no estem només llegint un recurs ja existent

### Pas 3. Definir l'entrada

Ara escriviu quins camps espereu.

Exemple:

```json
{
  "full_name": "Maria Ferrer",
  "id_number": "12345678A",
  "appointment_date": "2026-10-03",
  "email": "maria@example.com"
}
```

La pregunta important és:

- quins camps són obligatoris?
- quins poden faltar però enviar el cas a revisió?

### Pas 4. Definir la resposta correcta

Ara penseu com hauria de respondre la API quan tot va bé.

Exemple:

```json
{
  "status": "valid",
  "decision": "continue",
  "message": "La sol.licitud compleix les regles mínimes de validació"
}
```

El valor d'esta resposta no és només que siga llegible per una persona. També hauria de ser usable per altres serveis.

### Pas 5. Definir la resposta d'error

Ara penseu què passa si falta un camp crític.

Exemple:

```json
{
  "status": "invalid",
  "decision": "stop",
  "error": "Falta el camp id_number"
}
```

I a més cal decidir un codi d'estat coherent, com `400`.

### Pas 6. Comparar una API clara amb una API confusa

Ara feu l'exercici contrari.

Imagineu una API que:

- sempre torna `200`
- a vegades envia text lliure
- a vegades envia JSON amb camps diferents

Pregunteu-vos:

- la podria consumir bé un workflow?
- un dashboard sabria interpretar el resultat?
- un altre equip entendria ràpidament què esperar?

Esta comparació ajuda molt a entendre per què la coherència és tan important com el funcionament tècnic.

### Pas 7. Tancar amb una prova de caixa negra

Per acabar, escriviu tres casos:

- un cas vàlid
- un cas invàlid
- un cas incomplet però revisable

I indiqueu:

- entrada
- resposta esperada
- codi d'estat esperat

### Què hauria d'aprendre l'alumnat

- que una API és un contracte extern, no una funció interna
- que l'entrada, l'eixida i els errors s'han de pensar explícitament
- que la coherència fa la integració molt més fàcil

### Criteri docent

Si un altre equip pot llegir la definició de l'endpoint i saber què enviar, què rebre i què pot fallar, la API ja està ben plantejada a nivell bàsic.

## Resum final

Una bona `API REST` no és la que "funciona al meu ordinador", sinó la que:

- és coherent
- és previsible
- torna respostes útils
- i facilita la integració entre peces del sistema

## Com portar-ho a aula

- P1: usar-la per exposar classificació o consulta simple
- P4: usar-la per a validació d'entrada o integració amb workflow
- P5: usar-la quan calga unir serveis o oferir lectura estructurada a altres capes
- criteri docent: si un altre equip no pot entendre què enviar i què esperar, l'API encara no està prou ben definida

## Pràctica guiada suggerida

1. Escriu un endpoint per a una operació del projecte.
2. Defineix quina entrada necessita.
3. Escriu una resposta correcta i una incorrecta.
4. Indica quin codi d'estat hauries de tornar en cada cas.
