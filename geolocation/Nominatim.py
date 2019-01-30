import urllib
import json

# Classe criada para utilização do mecanismo de busca para o OpenStretMaps 'Nominatim'
class Nominatim:
    def __init__(self):
        self._json = None
    
    # Método query que retorna resposta da consulta ao OpenStretMaps de uma determinada localidade
    def query(self, query, endpoint = "https://nominatim.openstreetmap.org/search?format=json&q="):
        response = urllib.urlopen(endpoint + urllib.quote_plus(query, safe=''))
        self._json = json.load(response)

    # Método que retorna um id para a área buscada baseada baseado no id retornado pelo OSM
    def areaId(self):
        for d in self._json:
            if 'osm_type' in d and d['osm_type'] == 'relation' and 'osm_id' in d:
                return 3600000000 + int(d['osm_id'])
        return None
