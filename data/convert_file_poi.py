import json

list_pois = []

with open("sp_pois.json") as poi_data_file:
    line = poi_data_file.readline()
    with open("sp_pois_convert.json", "w") as poi_convert:

        while line:
            if line != "":
                line_json = eval(line)
                data = {
                    "item_id": line_json['gPlusPlaceId'],
                    "name": line_json['name'],
                    "longitude": line_json['gps'][1],
                    "latitude": line_json['gps'][0],
                }
                list_pois.append(data)
            line = poi_data_file.readline()
        
        json.dump(list_pois, poi_convert)

    
