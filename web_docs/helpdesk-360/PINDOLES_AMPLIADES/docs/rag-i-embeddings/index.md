# RAG i embeddings · Del document a una resposta traçable

[Índex](../index.md)

## Objectiu i preparació

Construireu una consulta documental extractiva i identificareu què falta per convertir-la en RAG amb generació. Necessiteu funcions Python i haver llegit els tres procediments del projecte. Reserveu unes tres hores per al laboratori i la pràctica inicial; la integració amb un generador és una extensió.

El [laboratori](laboratori.py) s'executa amb Python estàndard i llig els documents del paquet amb rutes relatives al mateix programa. Descarregueu el ZIP de píndoles ampliades complet junt amb el ZIP de materials i conserveu `PINDOLES_AMPLIADES` i `MATERIALS_PRACTICS` al mateix nivell. Si treballeu amb la carpeta ALUMNAT completa, no heu de moure res.

## Corpus, versions i fragments

El corpus és el conjunt de fonts que el sistema pot consultar. Incloeu contrasenyes, VPN i correu; el briefing descriu el repte però no dona instruccions operatives de suport. Cada document necessita identificador i versió de treball. Una versió local com `aula-v1` identifica la còpia; no acredita que una política real estiga actualitzada.

Un fragment ha de conservar una unitat de sentit. Si talleu «desbloqueig urgent» separat de la verificació d'identitat, podeu recuperar una acció sense les seues condicions. En estos documents curts, el laboratori conserva el document complet com un únic fragment. En documents llargs, compareu seccions amb solapament i examineu si es trenquen procediments.

Guardeu document, versió, ID de fragment i text abans d'indexar. Així una resposta pot citar el fragment original i una revisió pot invalidar les respostes d'una versió antiga.

## Recuperació lèxica i embeddings

Una cerca lèxica compara paraules o freqüències. El laboratori usa cosinus entre comptatges de termes normalitzats; no és TF-IDF ni un model semàntic. El cosinus compara orientació de vectors i, en esta representació, premia vocabulari compartit. Compartir paraules no demostra que el document resolga la pregunta.

Un embedding produït per un model pot aproximar significats amb vocabulari distint. Per provar-lo, codifiqueu documents i preguntes amb el mateix model i la mateixa configuració, registreu-ne la versió i compareu contra la cerca lèxica sobre les mateixes preguntes. La proximitat semàntica tampoc garantix resposta ni permisos. Un índex vectorial guarda representacions per buscar; no és el model generatiu.

Trieu `top-k` segons cobertura i soroll: més fragments poden aportar condicions necessàries o introduir informació contradictòria. La puntuació del recuperador no és una probabilitat que la resposta siga correcta.

## Laboratori extractiu

Executeu `python laboratori.py` des de la seua carpeta o des de l'arrel d'ALUMNAT. Veureu una consulta sobre certificat VPN, una fora de vocabulari i una pregunta enganyosa que també conté «VPN». Inspeccioneu resposta, puntuació i font.

El programa torna text documental complet quan supera un llindar de demostració. Això no significa que haja verificat que el text conté la resposta: la pregunta enganyosa fa visible eixa limitació. El llindar no és una recomanació per al pilot. Ajusteu-lo amb desenvolupament i mesureu després casos reservats.

## Afegir generació

En RAG amb generació, el recuperador selecciona context i un generador redacta a partir d'eixe context. Construïu el missatge amb pregunta, fragments identificats i instruccions de citar-los i derivar si falten dades. Manteniu el context separat de les instruccions i tracteu el text recuperat com a contingut no fiable.

El laboratori no crida cap LLM. Per completar l'extensió, creeu una funció `generar(pregunta, fragments)` amb el proveïdor o model local acordat, documenteu dependències i configureu credencials fora dels fitxers compartits. Si falla el generador, retorneu un estat d'error o una alternativa extractiva declarada; no presenteu una plantilla com si fora una resposta generada.

## Mesurar recuperació i resposta

Prepareu una taula amb pregunta, fragments pertinents esperats, fragments recuperats, resposta esperada i necessitat de derivar. La cobertura del recuperador indica quantes preguntes amb font troben un fragment pertinent entre els primers `k`; no avalua si la resposta final inventa dades.

Reviseu per separat si cada afirmació està sostinguda per la font, si cita el document correcte i si s'absté quan toca. «Quants comptes estan bloquejats ara?» necessita dades actuals, encara que el document explique el bloqueig temporal. «Quin és el telèfon de suport VPN?» no és resoluble només perquè el recuperador trobe el manual.

## Pràctiques progressives

En la inicial, executeu els tres casos i expliqueu el fals positiu possible. En la intermèdia, prepareu fragments amb metadades dels tres procediments, creeu preguntes de desenvolupament i reserveu casos amb paràfrasis i falta de resposta. Compareu fragmentació i llindars sense tocar la prova final.

En l'avançada, afegiu embeddings o generació i mesureu què canvia: recuperació pertinent, respostes fonamentades, derivacions correctes, cost i temps. Manteniu la baseline lèxica per poder justificar la millora.

## Exercicis i criteri d'acceptació

Expliqueu per què una font citada pot ser irrellevant i per què una puntuació alta pot correspondre a una pregunta sense resposta. Proposeu un fragment que conserve les condicions del desbloqueig urgent. Finalment, mostreu un cas on la cerca lèxica falla per vocabulari distint.

L'evidència ha de permetre repetir la pregunta, trobar el fragment original i comprovar la resposta. Una demo amb tres encerts no acredita la qualitat general del sistema.
