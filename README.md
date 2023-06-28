# RailNL
Deze case gaat over het maken van een lijnvoering van intercitytreinen door Nederland met als doel de hoogste kwaliteit verkrijgen. De lijnvoering mag uit maximaal 20 trajecten bestaan binnen een tijdsframe van 3 uur. Om tot een optimale oplossing te komen is er eerst gebruik gemaakt van de treinvoering door Noord-Holland en Zuid-Holland.


### Vereisten
Deze codebase is vollgedig geschreven in Python 3.9. In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren vis pip dmv. de volgende instructie:

```pip install -r requirements.txt``` 

Of via conda: 

```conda install --file requirements.txt```

### Gebruik
Het aanroepen van de code waarmee er oplossingen van de case worden gegeven is:

```python main.py```

Dit geeft een menu met verschillende experimenten waaruit gekozen kan worden. Welk(e) algortime(n) gebruikt worden, hangt af van het experiment.
De resultaten worden in csv-format gedumpt in resultaten. In hetzelfde mapje komt ook de visualisatie (plot) van de resultaten terecht.

De visualisatie van het netwerk wordt alleen gedaan als er niet verschillende algoritmen in één experiment worden gebruikt. Deze is te vinden in **/visualisation/plots**.
### Structuur

De hierop volgende lijst beschrijft de belangrijkste mappen en files in het project, en waar je ze kan vinden:

- **/code**: bevat alle code voor de datastructuur van dit project.
- **/data**: bevat de verschillende databestanden die nodig zijn om de lijnvoering te maken en te visualiseren.
- **/experiments**: bevat de code voor de experimenten.
- **/results**: bevat de resultaten van de experimenten.
- **/visualisation**: bevat de code voor de visualisatie en afbeeldingen van netwerken.
- **main.py**: hoofd code die alle modules importeert en als eerste gerund moet worden.
- **requirements.txt**: bevat alle benodigde packages om te code te laten draaien.


## Team: JAS
* Jens van der Weide
* Anna Nijmeijers
* Sebastiaan Smit
