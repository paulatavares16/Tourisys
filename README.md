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

## Executando com dataset Google Local Reviews

### Gerando os dados

O dataset engloba o mundo inteiro, é necessário filtrar o país desejado para melhorar tempo de execução das próximas buscas por cidades, no momento o script está configurado para filtrar as informações referentes ao Brasil.

```

python data_filter.py

```

Como output serão criados os arquivos: brasil_reviews.json, brasil_users.json e poi_brasil.json

Para gerar os dados referentes a uma cidade é necessário executar o script indicado a baixo. No momento o arquivoe está configurado para gerar informações para São Paulo.

```

python data_filter_sp.json

```

### Convertendo os dados

É necessário converter os dados para o formato esperado pela função do GraphLab. Para isso é executado o script abaixo:

```
python convert_file_poi.py

```

### Executando o algorítimo

Para a execução do sistema é necessário adicionar um ponto de partida, de preferência na cidade utilizada na filtragem, no arquivo [config.py](config.py)

```

user_location = {'lat': -23.5489, 'lng': -46.6388} # É a posição inicial em SP

```

Depois basta executar o arquivo principal

```

python main.py

```
