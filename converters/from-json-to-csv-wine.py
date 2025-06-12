#This file exists to convert the .json files that contain the wines and all their information 
#into csv files that can be directly uploaded into bubble.
import json
import csv

#Load the JSON file
with open('wines.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

#Open a CSV writer
with open('output.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    #Create the names of each category
    fieldnames = ['id', 'ITM8', 'EAN', 'name', 'region', 'country', 'year', 'type', 'grape', 'price', 'rating', 'descriptionFr', 'descriptionEng', 'image', 'bestseller', 'cheese', 'alcohol_percentage']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    #Put each items information in the correct place.
    for item in data:
        #The next line is used to transform a list into a json formatted list that can be inputed into the csv file.
        cheese_json = json.dumps(item.get('cheese', []), ensure_ascii=False)
        writer.writerow({
            'id': item.get('id'),
            'ITM8': item.get('ITM8'),
            'EAN': item.get('EAN'),
            'name': item.get('name'),
            'region': item.get('region'),
            'country': item.get('country'),
            'year': item.get('year'),
            'type': item.get('type'),
            'grape': item.get('grape'),
            'price': item.get('price'),
            'rating': item.get('rating'),
            'descriptionFr': item.get('description'),
            'descriptionEng': item.get('description_en'),
            'image': item.get('image'),
            'bestseller': item.get('bestseller'),
            'cheese': cheese_json,
            'alcohol_percentage': item.get('alcohol_percentage'),
        })
