# Dades de BiciTierra Market

**Dades íntegrament sintètiques per a docència.** No representen persones, vendes, campanyes ni preus observats d’una empresa real. La data de tall del cas és el **30 de juny de 2026**, independentment de la data real de la classe.

## Quin fitxer he d’obrir?

| Fitxer | Contingut | Ús |
|---|---|---|
| [sales_history.csv](sales_history.csv) | 1.188 files, 66 mesos, gener 2021–juny 2026 | EDA i predicció mensual d’unitats |
| [customers.csv](customers.csv) | 2.000 clients, fotografia a 30/06/2026 | Segmentació de comportaments |
| [sales_forecast_input.csv](sales_forecast_input.csv) | 18 combinacions per a juliol de 2026, sense vendes ni ingressos | Aplicar el model a un mes encara desconegut dins del cas |

Comença pels dos primers. El tercer s’usa després de validar el model. Els fitxers són UTF-8, separats per comes; els decimals usen punt i els nuls són cel·les buides.

## Què representa cada fila?

**Vendes:** un mes × canal (`store`, `ecommerce`) × línia (`urban`, `mountain`, `electric`) × regió (`coast`, `inland`, `metro`). Hi ha 18 sèries completes de 66 mesos. La clau són estos quatre camps; no s’ha de sumar més d’una vegada la mateixa fila.

**Clients:** una persona fictícia identificada amb una clau única, amb compres dels últims 12 mesos. És una mostra independent per a segmentació, no el llibre de transaccions de les vendes agregades. No hi ha una clau que permeta unir clients i vendes fila a fila. La suma d’`annual_spend` no ha de coincidir amb `revenue`.

## Quina predicció fem?

**Objectiu principal:** predir `sales_units` del mes següent abans de començar eixe mes, per cada canal, producte i regió. Són vendes realitzades, limitades per l’estoc; no són demanda total si hi ha ruptura d’estoc.

**Disponibles abans del mes:** `month`, `channel`, `product_line`, `region`, `marketing_budget`, `planned_discount`, `stock_units`, `list_price`, `campaign`, `days_in_month`. L’estoc és el disponible a l’inici; en esta simulació no hi ha reposició durant el mes.

**Només conegudes en tancar el mes:** `marketing_spend`, `avg_discount`, `website_sessions`, `sales_units`, `revenue`, `closing_stock_units`, `stockout`. No uses estos camps del mateix mes com a predictors anticipats. Sí que pots calcular retards amb dades de mesos anteriors de la mateixa sèrie.

En particular, predir `sales_units` amb `revenue` seria usar una dada que incorpora directament la resposta. La relació comptable és `revenue = sales_units × list_price × (1 − avg_discount)`, amb arrodoniment a cèntims. El descompte real està ocult en algunes files com a exercici de qualitat.

## Ordre de treball i separació temporal

1. **EDA:** comprova nuls, claus, cobertura mensual i patrons per producte/canal/regió.
2. **Entrenament:** mesos fins a desembre de 2024. Si uses `lag_12`, el primer any actua com a escalfament i l’entrenament efectiu comença en gener de 2022.
3. **Validació:** gener–desembre de 2025, per comparar models i triar paràmetres.
4. **Prova final:** gener–juny de 2026, una sola avaluació després de fixar decisions.
5. **Aplicació:** juliol de 2026 amb `sales_forecast_input.csv`; el resultat real no està inclòs.

Separa mesos complets: totes les sèries d’un mes han d’anar al mateix període. Evita una partició aleatòria de files. Ajusta imputació i transformacions només amb entrenament. Usa MAE en unitats i WAPE sobre la suma d’unitats reals.

Els retards de la prova representen **predicció d’un mes vista amb actualització mensual**: quan predim juny, maig ja és conegut. No equival a predir sis mesos simultàniament al desembre. No uses dades de gener–juny per afinar el model abans de fer la prova final.

## Què hi ha per aprendre?

- Estacionalitat diferent per línia, creixement gradual i diferències entre canals i regions.
- Campanyes, pressupost i descomptes amb efectes sobre les vendes.
- Variabilitat aleatòria, dependència temporal i episodis d’estoc insuficient.
- Clients amb comportaments solapats, devolucions, antiguitat i recència.
- Nuls controlats: en vendes, 18 en despesa real, 24 en descompte real, 18 en sessions, 12 en pressupost i 12 en descompte previst; en clients, 30 en despesa anual, 20 en edat i 20 en recència. No hi ha claus ni objectius absents ni duplicats intencionats.

Els patrons són hipòtesis simulades, no estimacions causals ni evidència sobre el mercat real. No hi ha una etiqueta de segment «correcte» ni una resposta única de clustering. En clients, `annual_spend` deriva de freqüència × tiquet: considera la redundància abans d’usar totes tres variables en clustering.

Consulta el [diccionari de dades](DICCIONARI_DADES.md) per a unitats, camps i valors vàlids. Per treballar, usa els CSV d’esta carpeta.
