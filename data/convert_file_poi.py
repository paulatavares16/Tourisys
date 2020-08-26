import json

list_pois = []

place_categories = {}
category_mapping = {}

with open("map-reviews-cat.json") as mapping:
    category_mapping = json.load(mapping)
    print(category_mapping)

with open("tmp_place_cat.json") as tmp_cat_data:
    line = tmp_cat_data.readline()
    data = json.loads(line)
    for record in data:
        gPlusPlaceId = record['gPlusPlaceId']
        mapped_categories = []
        for cat in (record['categories'] or []):
            if cat in category_mapping:
                mapped = category_mapping[cat]
                if mapped not in mapped_categories:
                    mapped_categories.append(category_mapping[cat])
        if len(mapped_categories) > 0:
            place_categories[gPlusPlaceId] = mapped_categories
    
with open("ssa_pois.json") as poi_data_file:
    line = poi_data_file.readline()
    with open("ssa_pois_convert.json", "w") as poi_convert:

        while line:
            if line != "":
                line_json = eval(line)
                gPlusPlaceId = line_json['gPlusPlaceId']
                if gPlusPlaceId in place_categories:
                    data = {
                        "item_id": gPlusPlaceId,
                        "name": line_json['name'],
                        "category": ','.join(place_categories[gPlusPlaceId]),
                        "longitude": line_json['gps'][1],
                        "latitude": line_json['gps'][0],
                    }
                    list_pois.append(data)
            line = poi_data_file.readline()
        
        json.dump(list_pois, poi_convert)

list_reviews = []

with open("ssa_reviews.json") as reviews_data_file:
    line = reviews_data_file.readline()
    with open("ssa_reviews_convert.json", "w") as reviews_convert:

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

with open("ssa_users.json") as users_data_file:
    line = users_data_file.readline()
    with open("ssa_users_convert.json", "w") as users_convert:

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
    
