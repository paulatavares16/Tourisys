import json

with open("brasil_reviews.json") as file:
  line = file.readline()
  with open("categories.json", "w") as cat_file:
    cat_list = []
    while line:
      if line != EOF:
        line_json = eval(line)
        cat_list.append(line_json['categories'])
      line = file.readline()
    json.dump(cat_list, cat_file)
    
