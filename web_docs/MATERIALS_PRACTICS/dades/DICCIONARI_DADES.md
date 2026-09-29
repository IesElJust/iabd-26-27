# Diccionari de dades · BiciTierra Market

Tots els valors són sintètics. Imports en EUR; proporcions entre 0 i 1 (0.15 significa 15%). Nul no significa zero. Els períodes són de la simulació.

## Vendes mensuals

| Camp | Tipus / unitat | Definició i disponibilitat |
|---|---|---|
| month | text YYYY-MM | Mes que es vol predir; conegut abans |
| channel | categoria | `store` o `ecommerce`; conegut abans |
| product_line | categoria | `urban`, `mountain`, `electric`; conegut abans |
| region | categoria | `coast`, `inland`, `metro`; conegut abans |
| marketing_spend | decimal EUR | Despesa real del mes; al tancament; pot faltar |
| avg_discount | proporció | Descompte efectiu del mes; al tancament; pot faltar |
| stock_units | enter unitats | Disponibilitat inicial del mes; coneguda abans. No és estoc final |
| website_sessions | enter visites | Sessions del mes atribuïdes a la cel·la comercial, també de suport a botiga; al tancament; pot faltar |
| sales_units | enter unitats | Objectiu: unitats venudes; al tancament, limitades per l’estoc |
| revenue | decimal EUR | Ingressos nets de descompte, sense impostos; al tancament; no predictor d’unitats del mateix mes |
| marketing_budget | decimal EUR | Pressupost aprovat abans del mes; pot faltar en l’extracte històric |
| planned_discount | proporció | Descompte previst abans del mes; pot faltar en l’extracte històric |
| list_price | decimal EUR/unitat | Preu de tarifa representatiu fixat abans del mes |
| campaign | categoria | Pla simulat: `none`, `spring`, `summer`, `black_friday`, `christmas`; conegut abans, no calendari comercial real |
| days_in_month | enter dies | Nombre de dies naturals del mes; conegut abans |
| closing_stock_units | enter unitats | `stock_units - sales_units`; al tancament; no predictor anticipat |
| stockout | enter 0/1 | 1 si la demanda simulada supera la disponibilitat; només al tancament |

No hi ha reposició intramensual. Per això `sales_units <= stock_units` i l’estoc final mai és negatiu. No es publica la demanda no servida; el fitxer permet explicar la censura per estoc, no avaluar una predicció exacta de demanda latent.

## Entrada de predicció

`sales_forecast_input.csv` usa els deu camps coneguts abans del mes: `month`, `channel`, `product_line`, `region`, `stock_units`, `marketing_budget`, `planned_discount`, `list_price`, `campaign`, `days_in_month`.

Conté juliol de 2026 i no inclou columnes d’objectiu buides: no s’ha de confondre absència de resultat amb vendes zero. Els retards s’obtenen de l’històric amb la clau completa i el mes correcte.

## Clients

| Camp | Tipus / unitat | Definició |
|---|---|---|
| customer_id | identificador | Clau fictícia única; excloure-la del clustering |
| age | enter anys | Edat entre 18 i 79; pot faltar |
| city | categoria | Gandia, Oliva, Sueca, Alzira, Tavernes o Carcaixent; ubicació fictícia |
| channel_preference | categoria | `store` o `ecommerce` |
| annual_spend | decimal EUR | Import acumulat de comandes dels últims 12 mesos, abans de devolucions; pot faltar |
| avg_order_value | decimal EUR/comanda | Tiquet mitjà dels últims 12 mesos |
| orders_last_12m | enter comandes | Comandes en els últims 12 mesos; mostra de clients amb almenys una compra |
| returns_ratio | proporció | `returned_orders_last_12m / orders_last_12m`, arrodonit a quatre decimals |
| bike_interest | categoria | `urban`, `mountain`, `electric` o `service` |
| service_interest | categoria | `low`, `medium`, `high` |
| snapshot_date | text YYYY-MM-DD | Data de tall 2026-06-30; comuna a tota la mostra |
| tenure_months | enter mesos | Antiguitat de 2 a 120 mesos |
| days_since_last_order | enter dies | Recència a la data de tall, entre 0 i 364; pot faltar |
| returned_orders_last_12m | enter comandes | Nombre de comandes amb devolució; no supera el de comandes |

`annual_spend = avg_order_value × orders_last_12m` amb arrodoniment a cèntims. Si falta despesa es pot reconstruir en este cas simulat; cal justificar-ho. No hi ha dades posteriors a la fotografia ni etiqueta de compra futura: este CSV serveix per a segmentació, no per validar predicció de churn o compres futures.
