import io
import webbrowser
import os
from jinja2 import FileSystemLoader, Environment, select_autoescape
from config import google_api_key

class Route:
    def __init__(self, latitudes, longitudes):
        self._latitudes = latitudes
        self._longitudes = longitudes

    def _waypoints(self):
        endpoint = 'var waypoints = [';
        for lat, lng in zip(self._latitudes, self._longitudes):
            endpoint += '{lat: %s, lng: %s}, ' % (lat, lng)
        endpoint = endpoint[:-2]
        endpoint += ']'
        return endpoint

    def map(self):
        loader = FileSystemLoader('routes')
        env = Environment (loader=loader, autoescape=select_autoescape(['html', 'xml']))
        template = env.get_template('route_sample.html')
        
        mapsUrl = "https://maps.googleapis.com/maps/api/js?key=" + google_api_key + "&callback=initMap"

        with io.open('routes/location.js', 'w', encoding='utf8') as location_file:
            location_file.write(unicode(self._waypoints()))

        with io.open('routes/route.html', 'a', encoding='utf8') as route_file:
            route_file.write(template.render(mapsUrl=mapsUrl))
        
        webbrowser.open('file://' + os.path.realpath('routes/route.html'))