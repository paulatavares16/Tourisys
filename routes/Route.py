import io
import webbrowser
import os
from jinja2 import FileSystemLoader, Environment, select_autoescape
from config import google_api_key, user_location
from clusterization import clusterization_list

class Route:
    def __init__(self, latitudes, longitudes):
        self._latitudes = latitudes
        self._longitudes = longitudes

    def _waypoints(self, list_points):
        waypoints = []
        for lat, lng in list_points:
            waypoints.append({'lat': lat, 'lng': lng})
        return waypoints
    
    def write_csv(self):
        list_points = zip(self._latitudes, self._longitudes)
        file_cluster = io.open('routes/file_cluster.csv', 'w')
        for point in list_points:
            file_cluster.write(unicode(point[0]) + ',' + unicode(point[1]) + '\n')

    def separete_rota(self, clust_num, list_clust):
        list_points = zip(self._latitudes, self._longitudes)
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
            

    def map(self):
        self.write_csv()

        list_clust = clusterization_list()

        for ind in range(0,3):
            list_points = self.separete_rota(ind, list_clust)
            waypoints = self._waypoints(list_points)
            self.plot_map(ind, waypoints)

