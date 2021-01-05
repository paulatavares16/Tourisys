import json

brasil_lower_lat = -33.7683777809
brasil_lower_long = -73.9872354804
brasil_upper_lat = 5.24448639569
brasil_upper_long = -34.7299934555

br_places = set()
br_users = set()

with open("poi_brasil") as poi_data_file:
    line = poi_data_file.readline()

    while line:
        line_json = eval(line)
        if line_json['gps'] and line_json['gps'][0] >= brasil_lower_lat and line_json['gps'][1] >= brasil_lower_long and line_json['gps'][0] <= brasil_upper_lat and line_json['gps'][1] <= brasil_upper_long:
            print(line_json['name'])

        line = poi_data_file.readline()


br_places = set()
br_users = set()

# gPlusUserId

with open("poi_brasil.json") as poi_data_file:
    line = poi_data_file.readline()

    while line:
        line_json = eval(line)
        if line_json['gps'] and line_json['gps'][0] >= brasil_lower_lat and line_json['gps'][1] >= brasil_lower_long and line_json['gps'][0] <= brasil_upper_lat and line_json['gps'][1] <= brasil_upper_long:
            # print('Entrou')
            br_places.add(line_json['gPlusPlaceId'])
        # else:
        #     print(line_json)

        line = poi_data_file.readline()

print('Comecou a bagaceira dos reviews')    
with open("review.json") as poi_data_file:
    line = poi_data_file.readline()

    with open("brasil_reviews.json", "w") as review_data_file:
        while line:
            line_json = eval(line)
            if line_json['gPlusPlaceId'] in br_places:
                br_users.add(line_json['gPlusUserId'])
                review_data_file.write(line)
                review_data_file.write('\n')

            line = poi_data_file.readline()

print('Comecou a bagaceira dos usuarios')    
with open("user.json") as poi_data_file:
    line = poi_data_file.readline()

    with open("brasil_users.json", "w") as review_data_file:
        while line:
            line_json = eval(line)
            if line_json['gPlusUserId'] in br_users:
                review_data_file.write(line)
                review_data_file.write('\n')

            line = poi_data_file.readline()
            

        
        

        