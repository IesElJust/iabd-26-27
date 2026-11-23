# Diccionari de dades

Cada fila representa un ticket del conjunt de pràctica del projecte. No incorporeu dades personals reals.

| Camp | Significat | Ús |
|---|---|---|
| ticket_id | Identificador del ticket | Traçabilitat; no és predictor |
| canal | Via d'entrada | Exploració |
| client_sector | Sector del client | Exploració |
| text_ticket | Descripció de la incidència | Entrada del classificador |
| urgencia_reportada | Urgència declarada | Revisar amb criteris operatius |
| departament_sospitat | Etiqueta inicial de departament | Objectiu provisional; cal revisar-la |
| estat | Estat de tramitació | Normalitzar abans d'analitzar |

No useu l'etiqueta objectiu com a entrada. Les etiquetes sospitades no equivalen a una veritat revisada. Documenteu les correccions. La mida reduïda limita la interpretació de mètriques; els quasi duplicats han de quedar en la mateixa partició.
