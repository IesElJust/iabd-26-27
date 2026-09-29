# Model de taules · BiciTierra Market

## Vendes

`sales_history.csv` és una taula de fets mensual amb clau `month + channel + product_line + region`. Es pot relacionar amb dimensions de calendari, canal, producte i regió. Suma unitats i ingressos; no sumes preus ni percentatges. Per a un descompte agregat ponderat, justifica els pesos i el tractament de nuls.

`sales_forecast_input.csv` conté inputs de juliol de 2026, no vendes reals. Guarda les prediccions en una taula separada amb la mateixa clau i una marca clara de previsió. No representes el mes futur com a venda zero.

## Clients

`customers.csv` és una fotografia independent de 2.000 clients a 30/06/2026. No té clau transaccional compartida amb vendes. Mostra els segments en una vista separada; no faces una unió molts-a-molts per canal o regió ni esperes que la despesa sume els ingressos de vendes.

Consulta el [diccionari](../dades/DICCIONARI_DADES.md) per a granularitat, unitats i disponibilitat dels camps.
