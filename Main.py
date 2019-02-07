# -*- coding: utf-8 -*-
from geolocation.Nominatim import *
from poi.OverlayData import *
from poi.GMapsData import *
from recsys.RecSys import *

# Instânciamento da classe do Nominatim 
# utilizada para realizar buscas com o OSM
nominatim = Nominatim();
# Query que retorna informações de uma localidade segundo OSM
nominatim.query("Salvador,Bahia,Brazil")
# Determinação de id da área buscada/determinada
areaIdSalvador = nominatim.areaId()

# Instancia da classe na qual é possível utilizar OverlayPass 
# chamando em senguida metodo que da origem a lista de poi's com o id da area solicitada
overlayData = OverlayData()
overlayData.poiData(areaIdSalvador)

# Instancia da classe com funções para interações com o Google Maps
# chama função que gera lista de reviews, poi's e usuários
gMapsData = GMapsData()
gMapsData.data(overlayData.poiList)

gMapsData.json()

recSys = RecSys(user_data='data/user.json', item_data='data/poi.json', rating_data='data/review.json')
## Evaluates
recSys.itemSimilarity(eval=True)
# recSys.itemSimilarity(similarityType='cosine', eval=True)
# recSys.itemSimilarity(similarityType='pearson', eval=True)

# recSys.itemContent(attributes=['item_id', 'category'], splitAttribute='category', eval=True)
# recSys.itemContent(attributes=['item_id', 'category'], eval=True)
# recSys.itemContent(attributes=['item_id', 'latitude', 'longitude'], eval=True)
# recSys.itemContent(attributes=['item_id', 'category', 'latitude', 'longitude'], splitAttribute='category', eval=True)
# recSys.itemContent(attributes=['item_id', 'category', 'latitude', 'longitude'], eval=True)
# recSys.itemContent(attributes=['item_id', 'name'], eval=True)
# recSys.itemContent(attributes=['item_id', 'name', 'category'], splitAttribute='category', eval=True)
# recSys.itemContent(attributes=['item_id', 'name', 'category'], eval=True)
recSys.itemContent(splitAttribute='category', eval=True)
recSys.itemContent(eval=True)

## Recommends for new users
recent_data = gl.SFrame();
recent_data['user_id'] = ['99999']
recent_data['item_id'] = [59392558]
recent_data['rating'] = [0.8]
recSys.itemSimilarity(similarityType='pearson', newUsers=[99999], newObservationData=recent_data)
recSys.itemContent(newUsers=[99999], newObservationData=recent_data)

## Get similar items
recSys.itemSimilarity(similarityType='pearson', similarItem=[59224731])
recSys.itemContent(newUsers=[99999], similarItem=[59224731])
