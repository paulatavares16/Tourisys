# -*- coding: utf-8 -*-
from geolocation.Nominatim import *
from poi.OverlayData import *
from poi.GMapsData import *

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
print "Finalização da geração de data"