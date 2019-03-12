# Tourisys

Recommendation System for points of interest.

## Instalation

- Graphlab dependence:

```
GraphLab-Create==2.1
GraphLab-Create-License==2.1
```

To install GraphLab follow the instructions [here](https://turi.com/download/install-graphlab-create-command-line.html). Option 2 for virtualenv instalation.

Installing others dependences on virtualenv:

```
pip install -r requirements.txt
```

## Running

Instructions:

- In [config.py](config.py) add your Google API Key
- In [Main.py](Main.py), setting your query (place to search poins of interest in the region that you choose);
- Choose type of recommender (ItemSimilary or ItemContent and your attributes).
