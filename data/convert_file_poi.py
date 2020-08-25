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

list_reviews = []

with open("sp_reviews.json") as reviews_data_file:
    line = reviews_data_file.readline()
    with open("sp_reviews_convert.json", "w") as reviews_convert:

        while line:
            if line != "":
                line_json = eval(line)
                data = {
                    "item_id": line_json['gPlusPlaceId'],
                    "rating": line_json['rating'],
                    "user_id": line_json['gPlusUserId'],
                }
                list_reviews.append(data)
            line = reviews_data_file.readline()
        
        json.dump(list_reviews, reviews_convert)

list_users = []

with open("sp_users.json") as users_data_file:
    line = users_data_file.readline()
    with open("sp_users_convert.json", "w") as users_convert:

        while line:
            if line != "":
                line_json = eval(line)
                data = {
                    "user_id": line_json['gPlusUserId'],
                    "name": line_json['userName'],
                }
                list_users.append(data)
            line = users_data_file.readline()
        
        json.dump(list_users, users_convert)
    
