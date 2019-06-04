# -*- coding: utf-8 -*-
# Python Wrapper para acesso ao Overpass aPI
import overpy


class OverlayData:
    _categoryLink_art = [
        {'selector': '["amenity"="arts_centre"]', 'type': 'arts_centre'},
        {'selector': '["tourism"="gallery"]', 'type': 'gallery'},
        {'selector': '["tourism"="artwork"][artwork_type!~"statue"]', 'type': 'artwork'},
        {'selector': '["historic"~"^monument$|^memorial$"]', 'type': 'monument_memorial'},
        {'selector': '["tourism"="museum"]', 'type': 'museum'},
        {'selector': '["historic"="statue"]', 'type': 'statue'},
        {'selector': '["historic"][historic!~"memorial|monument|statue|castle"]', 'type': 'historic'},

    ]

    _categoryLink_entertainment = [
        {'selector': '["tourism"="attraction"]', 'type': 'attraction'},
        {'selector': '["tourism"="information"]', 'type': 'information'},
        {'selector': '["tourism"="theme_park"]', 'type': 'theme_park'},
        {'selector': '["tourism"="viewpoint"]', 'type': 'viewpoint'},
        {'selector': '["tourism"="zoo"]', 'type': 'zoo'},
        {'selector': '["leisure"="casino"]', 'type': 'casino'},
        {'selector': '["leisure"="gastro"]', 'type': 'gastro'},
        {'selector': '["tourism"="picnic_site"]', 'type': 'picnic'},

    ]

    _categoryLink = [
        {'selector': '["amenity"="arts_centre"]', 'type': 'arts_centre'},
        {'selector': '["leisure"="gastro"]', 'type': 'gastro'},
        # {'selector': '["tourism"="artwork"][artwork_type!~"statue"]', 'type': 'artwork'},
        {'selector': '["tourism"="attraction"]', 'type': 'attraction'},
        # {'selector': '["leisure"="casino"]', 'type': 'casino'},
        # {'selector': '["historic"="castle"]', 'type': 'castle'},
        {'selector': '["tourism"="gallery"]', 'type': 'gallery'},
        # {'selector': '["heritage"]', 'type': 'heritage'},
        # {'selector': '["historic"][historic!~"memorial|monument|statue|castle"]', 'type': 'historic'},
        {'selector': '["tourism"="information"]', 'type': 'information'},
        {'selector': '["historic"~"^monument$|^memorial$"]', 'type': 'monument_memorial'},
        {'selector': '["natural"="tree"]["monument"="yes"]', 'type': 'monumental_tree'},
        {'selector': '["tourism"="museum"]', 'type': 'museum'},
        # {'selector': '["tourism"="picnic_site"]', 'type': 'picnic'},
        # {'selector': '["leisure"="picnic_table"]', 'type': 'picnic'},
        {'selector': '["historic"="statue"]', 'type': 'statue'},
        {'selector': '["landmark"="statue"]', 'type': 'statue'},
        # {'selector': '["tourism"="artwork"]["artwork_type"="statue"]', 'type': 'statue'},
        {'selector': '["tourism"="theme_park"]', 'type': 'theme_park'},
        {'selector': '["tourism"="viewpoint"]', 'type': 'viewpoint'},
        # {'selector': '["landuse"="vineyard"]', 'type': 'vineyard'},
        # {'selector': '["man_made"="windmill"]', 'type': 'windmill'},
        # {'selector': '["man_made"="watermill"]', 'type': 'watermill'},
        {'selector': '["tourism"="zoo"]', 'type': 'zoo'},
    ]

    def __init__(self, timeout = 25):
        self._timeout = timeout
        self.poiList = []

    # Para cada categoria da qual será realizada a query as informações são registradas através do metodo abaixo
    def _saveInfo(self, elements, category):
        for element in elements or []:
            #Se não houver nenhum elemento já registrado na lista de poi's 
            if not any(d['id'] == element.id for d in self.poiList):
                poi = {}
                # São salvas as informações de lat e lon para node, e informações centrais de lat e lon para outros dois
                if element._type_value == 'node':
                    poi['latitude'] = float(element.lat)
                    poi['longitude'] = float(element.lon)
                else:
                    poi['latitude'] = float(element.center_lat)
                    poi['longitude'] = float(element.center_lon)
                # Para todos são salvos id's, nomes e tipo da categoria.
                poi['id'] = element.id
                poi['name'] = element.tags['name']
                poi['type'] = [category]
                self.poiList.append(poi)
            else:
                for d in self.poiList:
                    if d['id'] == element.id:
                        d['type'].append(category)

    def poiData(self, areaId, choice):
        print 'Querys do OverPass'
        # API de consulta que retorna data do OSM, de acordo com a query construida
        api = overpy.Overpass()
        choices = {
            "art": self._categoryLink_art,
            "entertainment": self._categoryLink_entertainment,
            "all": self._categoryLink,
        }

        # Construção das querys a serem consultadas, baseadas nas categorias determinadas no array
        for category in choices[choice]:
            # Todos os resultados das querys realizadas são adicionados na lista de elementos
            elements = []

            # Query referente a todos os nós contidos na bounding box determinada
            query = '[timeout:{}][out:json];' \
                        'area({})->.searchArea;' \
                        'node(area.searchArea);' \
                        'node._["name"]{};(._;>;);out center;'.format(self._timeout, areaId, category['selector']);
            try:
                result = api.query(query)
            except:
                print'Entrou na exceção1'
                time.sleep(1)
                result = api.query(query)                
            elements.extend(result.nodes)

            # Query referente a todos os caminhos que contém um nó na bounding box ou que a crusa
            query = '[timeout:{}][out:json];' \
                    'area({})->.searchArea;' \
                    'way(area.searchArea);' \
                    'way._["name"]{};(._;>;);out center;'.format(self._timeout, areaId, category['selector']);
            try:
                result = api.query(query)
            except:
                print'Entrou na exceção2'
                time.sleep(1)
                result = api.query(query)  
            elements.extend(result.ways)
            
            # Query referente a todos as relações da bounding box delimitada
            query = '[timeout:{}][out:json];' \
                    'area({})->.searchArea;' \
                    'rel(area.searchArea);' \
                    'rel._["name"]{};(._;>;);out center;'.format(self._timeout, areaId, category['selector']);
            try:
                result = api.query(query)
            except:
                print'Entrou na exceção3'
                time.sleep(1)
                result = api.query(query)  
            elements.extend(result.relations)
            print('Esse foi:'+ category['selector'])
            self._saveInfo(elements, category['type'])