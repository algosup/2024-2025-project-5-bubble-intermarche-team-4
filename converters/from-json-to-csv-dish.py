#This file exists to convert the .json files that contain the dishes and all their information 
#into csv files that can be directly uploaded into bubble.
import json
import csv

# Load the JSON file
with open('meal.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Open a CSV writer
with open('output.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    #Create the names of each category
    fieldnames = ['id', 'name', 'link', 'descriptionFr', 'descriptionEng', 'region', 'allergenes', 'wine', 'cheese', 'image']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    #Put each items information in the correct place.
    for item in data:
        #The three next lines are used to transform lists into json formatted lists that can be inputed into the csv file.
        allergens_json = json.dumps(item.get('allergenes', []), ensure_ascii=False)
        wine_json = json.dumps(item.get('wine', []), ensure_ascii=False)
        cheese_json = json.dumps(item.get('cheese', []), ensure_ascii=False)
        writer.writerow({
            'id': item.get('id'),
            'name': item.get('name'),
            'link': item.get('link'),
            'descriptionFr': item.get('descriptionFr'),
            'descriptionEng': item.get('descriptionEng'),
            'region': item.get('region'),
            'allergenes': allergens_json,
            'wine': wine_json,
            'cheese': cheese_json,   
            'image': item.get('image'),
        })
