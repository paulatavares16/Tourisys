# -*- coding: utf-8 -*-
import urllib
import json

# Classe criada para utilização do mecanismo de busca para o OpenStretMaps 'Nominatim'
class Nominatim:
    def __init__(self):
        self._json = None
    
    # Método que retorna resposta de uma consulta ao OpenStretMaps para uma determinada localidade
    def query(self, query, endpoint = "https://nominatim.openstreetmap.org/search?format=json&q="):
        print 'Processando query do nominatim - '
        print query, '\n'
        response = urllib.urlopen(endpoint + urllib.quote_plus(query, safe='')) # 'quote_plus' substitui espaços por +
        self._json = json.load(response)


    # Método que retorna um id para a área buscada baseada baseado no id retornado pelo OSM
    # Para achar o ID da relation do Overpass - API OSM - é necessário realizar a soma abaixo
    def areaId(self):
        print 'Definindo area ID'
        for d in self._json:
            if 'osm_type' in d and d['osm_type'] == 'relation' and 'osm_id' in d:
                return 3600000000 + int(d['osm_id'])
        return None
