# APIs REST · Exposa una consulta amb un contracte explícit

[Índex](../index.md)

## Objectiu i entorn

Creareu un endpoint local que valide una pregunta i torne una consulta documental estructurada. La pràctica dura aproximadament dos hores i requerix funcions Python i nocions de JSON. Useu l'entorn de treball del projecte; instal·leu `fastapi`, `uvicorn` i `httpx` per executar el laboratori i les comprovacions.

Descarregueu [app.py](app.py) i conserveu l'estructura del paquet junt amb el laboratori RAG. El programa reutilitza la consulta extractiva, no un generador ni el classificador de l'entrega. La documentació oficial explica la [validació del cos de la petició](https://fastapi.tiangolo.com/tutorial/body/).

## El contracte abans del servidor

Una API permet que un altre programa invoque una operació sense conéixer les funcions internes. `POST /consulta` rep JSON amb `pregunta` i torna JSON amb `estat`, `resposta`, `fonts` i `puntuacio`. El mètode POST permet enviar un cos estructurat; la ruta identifica l'operació.

```json
{"pregunta": "VPN error de certificat"}
```

HTTP 200 indica que la consulta s'ha processat, inclosa una derivació per falta de coincidència documental. No significa que el document haja resolt semànticament la pregunta. HTTP 422 indica que l'entrada no complix el contracte; HTTP 503, en este laboratori, que no es pot llegir el corpus. Un error de servidor no s'ha de convertir en una resposta documental inventada.

El contracte ha de separar una predicció de departament d'una consulta. Si afegiu `POST /classifica`, definiu també el camp d'entrada, l'etiqueta retornada i què feu amb text buit o vocabulari desconegut. No reutilitzeu la puntuació de recuperació com a confiança de classificació.

## Validar en la frontera

El model d'entrada exigix una cadena de text, la retalla i limita la longitud. Espais en blanc no formen una pregunta vàlida. Rebutjar camps addicionals ajuda a detectar noms equivocats abans d'arribar a la lògica. Estes validacions milloren el contracte, però no detecten una pregunta maliciosa ni establixen permisos.

El model d'eixida fixa els camps públics. L'aplicació no ha de tornar excepcions internes amb rutes de fitxers ni secrets. En cas de corpus absent, el laboratori retorna un missatge genèric i estat 503. Altres errors no previstos continuen sent errors de servidor que s'han de diagnosticar localment.

## Executar i provar

Des de la carpeta d'esta píndola:

```bash
python -m pip install fastapi uvicorn httpx
python -m uvicorn app:app --host 127.0.0.1 --port 8001
```

Obri `http://127.0.0.1:8001/docs` i usa la documentació interactiva per enviar la petició. També pots enviar-la des d'un altre terminal:

```bash
curl -X POST http://127.0.0.1:8001/consulta   -H 'Content-Type: application/json'   -d '{"pregunta":"VPN error de certificat"}'
```

Repetix amb una cadena buida, espais, un nombre, un camp mal escrit i una pregunta sense coincidències. Les primeres entrades han de donar 422 i l'última, 200 amb estat `derivar`. Compareu també una pregunta que conté VPN però demana una dada absent: l'API manté les limitacions del recuperador.

## De la funció a la integració

La funció documental funciona sense HTTP. Mantindre-la separada permet comprovar els resultats abans d'afegir la xarxa. En una aplicació més gran, carregueu índex i model quan arranca el servei en lloc d'ajustar-los en cada petició. Si compartiu recursos entre peticions, reviseu-ne la concurrència.

El laboratori escolta només en l'ordinador local. Per a un pilot compartit caldrà definir autenticació, autorització del corpus, límits de consum i desplegament. No exposeu el servidor docent directament a Internet ni confongueu l'accés a `/docs` amb autenticació.

## Pràctiques i evidència

En la pràctica inicial, registreu entrada, codi HTTP i cos de resposta per als sis casos. En la intermèdia, afegiu el vostre classificador amb un endpoint propi i una resposta tipada. En l'extensió, simuleu corpus absent i fallada del model: el client ha de distingir error temporal i falta de context.

Entregueu el contracte, instruccions d'arrancada i una taula de proves. Una altra persona ha de poder provar el servei sense llegir les funcions internes. Expliqueu per què una resposta 200 amb `derivar` és distinta d'una resposta 503 i què ha de mostrar la interfície en cada cas.
