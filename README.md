# RailNL
Deze case gaat over het maken van een lijnvoering van intercitytreinen door Nederland met als doel de hoogste kwaliteit verkrijgen. De lijnvoering mag uit maximaal 20 trajecten bestaan binnen een tijdsframe van 3 uur. Om tot een optimale oplossing te komen is er eerst gebruik gemaakt van de treinvoering door Noord-Holland en Zuid-Holland.

### Team: JAS
* Jens van der Weide
* Anna Nijmeijers
* Sebastiaan Smit

### Vereisten
Dit mooi maken
- Python 3.9.16
- Matplotlib 3.6.3
- Pandas 1.5.3
- Numpy 1.24.2
- tqdm 4.64.1
- csv 1.0
- via pip of conda requirements.txt installeren (eerst requirements.txt aanmaken)

### Gebruik
Het aanroepen van de code waarmee er oplossingen van de case worden gegeven is:

```python main.py```

Dit geeft de kwaliteit van de lijnvoering met gebruik verschillende algoritmes aan.

### Structuur

De hierop volgende lijst beschrijft de belangrijkste mappen en files in het project, en waar je ze kan vinden:

- **/code**: bevat alle code van dit project
  - **/code/algorithms**: bevat de code voor algoritmes
  - **/code/classes**: bevat de drie benodigde classes voor deze case
  - **/code/visualisation**: bevat de code voor de visualisatie
- **/data**: bevat de verschillende databestanden die nodig zijn om de lijnvoering te maken en te visualiseren
- **main.py**: hoofd code die alle modules importeert en als eerste gerund moet worden
- **requirements.txt**: bevat alle benodigde packages om te code te laten draaien
