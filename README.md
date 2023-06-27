# RailNL
Deze case gaat over het maken van een lijnvoering van intercitytreinen door Nederland met als doel de hoogste kwaliteit verkrijgen. De lijnvoering mag uit maximaal 20 trajecten bestaan binnen een tijdsframe van 3 uur. Om tot een optimale oplossing te komen is er eerst gebruik gemaakt van de treinvoering door Noord-Holland en Zuid-Holland.



## Aan de slag 

### Vereisten
Deze codebase is vollgedig geschreven in Python 3.9. In requirements.txt staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren vis pip dmv. de volgende instructie:

```pip install -r requirements.txt``` 

Of via conda: 

```conda install --file requirements.txt```

### Gebruik
Het aanroepen van de code waarmee er oplossingen van de case worden gegeven is:

```python main.py```

Dit geeft een menu met verschillende algoritmes waaruit gekozen kan worden. 
Vervlogens word de kwaliteit van de lijnvoering met gebruik van het gekozen algoritmes weergegeven. Het is mogelijk om te kizen voor de resultaten van een eerder uitgevoerd experiment of om het algoritme zelf te runnen. 

### Structuur

De hierop volgende lijst beschrijft de belangrijkste mappen en files in het project, en waar je ze kan vinden:

- **/code**: bevat alle code van dit project
  - **/code/algorithms**: bevat de code voor algoritmes
  - **/code/classes**: bevat de drie benodigde classes voor deze case
  - **/code/visualisation**: bevat de code voor de visualisatie
- **/data**: bevat de verschillende databestanden die nodig zijn om de lijnvoering te maken en te visualiseren
- **main.py**: hoofd code die alle modules importeert en als eerste gerund moet worden
- **requirements.txt**: bevat alle benodigde packages om te code te laten draaien


## Team: JAS
* Jens van der Weide
* Anna Nijmeijers
* Sebastiaan Smit
