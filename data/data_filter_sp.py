import json

#SP - SP
# sp_lower_lat = -23.784969
# sp_lower_long = -46.809319
# sp_upper_lat = -23.39566
# sp_upper_long = -46.36499

# Salvador
ssa_lower_long = -38.699435
ssa_lower_lat = -13.017395
ssa_upper_long = -38.303414
ssa_upper_lat = -12.733537


ssa_places = set()
ssa_users = set()

# gPlusUserId

with open("poi_brasil.json") as poi_data_file:
    line = poi_data_file.readline()
    with open("ssa_pois.json", "w") as review_data_file:
        while line:
            line_json = eval(line)
            if line_json['gps'] and line_json['gps'][0] >= ssa_lower_lat and line_json['gps'][1] >= ssa_lower_long and line_json['gps'][0] <= ssa_upper_lat and line_json['gps'][1] <= ssa_upper_long:
                # print('Entrou')
                review_data_file.write(line)
                ssa_places.add(line_json['gPlusPlaceId'])
            # else:
            #     print(line_json)

            line = poi_data_file.readline()

print('Comecou a bagaceira dos reviews')    
with open("review.json") as poi_data_file:
    line = poi_data_file.readline()

    with open("ssa_reviews.json", "w") as review_data_file:
        while line:
            line_json = eval(line)
            if line_json['gPlusPlaceId'] in ssa_places:
                ssa_users.add(line_json['gPlusUserId'])
                review_data_file.write(line)

            line = poi_data_file.readline()

print('Comecou a bagaceira dos usuarios')    
with open("user.json") as poi_data_file:
    line = poi_data_file.readline()

    with open("ssa_users.json", "w") as review_data_file:
        while line:
            line_json = eval(line)
            if line_json['gPlusUserId'] in ssa_users:
                review_data_file.write(line)

            line = poi_data_file.readline()
            

        
        

        