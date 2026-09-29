# Registre de validació

**Data:** 23 de setembre de 2026. **Abast:** onze unitats ampliades, onze demostracions Python, trenta-tres pràctiques guiades i trenta-tres reptes amb orientació.

## Comprovacions executades

S’han executat els onze programes sobre dades sintètiques en un entorn separat. Tots han acabat correctament. El notebook s’ha executat des d’un nucli nou; la primera execució es va bloquejar per la restricció de connexions locals de l’entorn de comprovació i la repetició autoritzada ha passat.

| Unitat | Resultat comprovat |
|---|---|
| Python | 3 lectures vàlides, 4 rebutjades; zero acceptat |
| Jupyter | Notebook creat i executat des de zero; mitjana 120 litres/dia |
| NumPy i pandas | 5 files després de la unió; 1 servei sense correspondència i 1 durada absent |
| Qualitat | 7 files auditades; 3 lectures vàlides sense duplicació |
| Visualització | PNG i SVG generats; 180 observacions repartides entre 3 edificis |
| scikit-learn | Comparació amb dummy, selecció per validació i avaluació en prova reservada |
| Validació | Dos talls amb dates disjuntes; 24 files de prova en 2026 |
| Clustering | Comparació de k, estabilitat entre llavors, DBSCAN i projecció PCA |
| XAI | Additivitat SHAP verificada; explicació LIME generada amb fidelitat local baixa, comentada en el text |
| Power BI | CSV i controls Python: 4 incidències, 200 minuts, mitjana 50 i resolució 75% |
| MLflow | Dos runs acabats, mètriques i models registrats en emmagatzematge local |

El codi mostrat en cada unitat coincidix amb el programa descarregable. La reformulació de format i comentaris s’ha comprovat preservant el mateix arbre de sintaxi. També han passat l’execució dels 19 fragments Python breus de la teoria, la comprovació dels 69 enllaços locals i la construcció de la presentació amb MkDocs en mode estricte. La figura del laboratori de visualització s’ha inspeccionat visualment.

## Límits de la comprovació

- Power BI Desktop no s’ha executat en este entorn: la importació, les mesures DAX i les interaccions visuals s’han de contrastar amb els controls durant la pràctica. No s’inclou cap PBIX.
- S’ha comprovat l’execució automàtica del notebook, no la seua interfície gràfica en tots els sistemes operatius.
- Les variants proposades en pràctiques i reptes són treball de l’alumnat; no s’han executat totes les possibles solucions.
- Els resultats amb dades sintètiques no són evidència de rendiment sobre dades reals. La prova temporal és mensual successiva i no una previsió conjunta de tots els mesos.
- Les versions fixades descriuen l’entorn comprovat; no s’afirma que siguen les últimes disponibles ni que qualsevol combinació futura siga compatible.

## Entorn executat

Python 3.10.12.

| Paquet | Versió |
|---|---|
| numpy | 2.2.6 |
| pandas | 2.3.3 |
| scikit-learn | 1.7.2 |
| matplotlib | 3.10.9 |
| seaborn | 0.13.2 |
| shap | 0.49.1 |
| lime | 0.2.0.1 |
| mlflow | 3.16.1 |
| nbformat | 5.11.1 |
| nbclient | 0.11.0 |
| ipykernel | 7.3.0 |

La presentació usa MkDocs Material 9.7.7. La instal·lació opcional de la interfície Notebook 7 no forma part de les onze execucions comprovades.
