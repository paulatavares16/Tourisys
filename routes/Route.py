# -*- coding: utf-8 -*-

import io
import webbrowser
import os
from jinja2 import FileSystemLoader, Environment, select_autoescape
from config import google_api_key, user_location
from clusterization import clusterization_list

from pymongo import MongoClient
import random

client = MongoClient(os.getenv('MONGODB_URI', 'mongodb://heroku_9mwpmxbf:kbjivvmpq9m46gr32u4t05bs8u@ds211708.mlab.com:11708/heroku_9mwpmxbf?retryWrites=false'))


class Route:
    def __init__(self, latitudes, longitudes, names):
        self._latitudes = latitudes
        self._longitudes = longitudes
        self._names = names

    def _waypoints(self, list_points):
        waypoints = []
        for lat, lng, name in list_points:
            waypoints.append({'lat': lat, 'lng': lng, 'name': name})
        return waypoints
    
    def write_csv(self):
        list_points = zip(self._latitudes, self._longitudes, self._names)
        file_cluster = io.open('routes/file_cluster.csv', 'w', encoding="utf-8")
        for point in list_points:
            file_cluster.write(unicode(point[0]) + ',' + unicode(point[1]) + ',')
            file_cluster.write(point[2].decode('utf-8'))
            file_cluster.write(u'\n')

    def separete_rota(self, clust_num, list_clust):
        list_points = zip(self._latitudes, self._longitudes, self._names)
        list_points_selct = []
        for ind in range(len(list_clust)):
            if list_clust[ind] == clust_num:
                list_points_selct.append(list_points[ind])

        return  list_points_selct

    
    def plot_map(self, ind, waypoints):
        # Carregar o template HTML
        loader = FileSystemLoader('routes')
        env = Environment (loader=loader, autoescape=select_autoescape(['html', 'xml']))
        template = env.get_template('route_sample.html')
        mapsUrl = "https://maps.googleapis.com/maps/api/js?key=" + google_api_key + "&callback=initMap"

        # with io.open('routes/location.js', 'w', encoding='utf8') as location_file:
        #     location_file.write(unicode(endpoint))
        
        with io.open('routes/route-%d.html'% ind, 'w', encoding='utf8') as route_file:
            route_file.write(template.render(mapsUrl=mapsUrl, conf_origin=user_location, waypoints=waypoints))
        if ind == 0:
            webbrowser.open('file://' + os.path.realpath('routes/route-%d.html'% ind))
            

    def map(self, userId):
        self.write_csv()
        db=client.heroku_9mwpmxbf
        
        list_clust = clusterization_list()
        suggestionId = random.random()*100000000000000000
        suggestion = {'user': userId, 'suggestionId': suggestionId}
        suggestion.setdefault('routes', [])

        for ind in range(0,3):
            list_points = self.separete_rota(ind, list_clust)
            waypoints = self._waypoints(list_points)
            aRoute = {'routeNumber': ind, 'waypoints': waypoints}
            suggestion['routes'].append(aRoute)
            
            # self.plot_map(ind, waypoints)
            
        db.suggestions.insert_one(suggestion)
