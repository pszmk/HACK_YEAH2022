from przemek_dir.modules.scoreManager import add_subScore
from pathlib import Path
import json

def resetDatabase():
    with open(Path(__file__).parent.parent/'data'/'user_items.json', 'w') as file:
        json.dump([], file, indent=4)

def addItem(item={}):
    new_item = {
        "name": None,
        "recommendation": None,
        "cathegory": None,
        "score": None,
        "usage": None,
        "source": None,
        "condition": None,
        "expiry_date": None,
        "quantity": None,
        "id": None
        }
    if not 'score' in item.keys():
        raise ValueError('The item lacks score!')
    add_subScore(item['score']-50)

    for key, val in item.items():
        if key in new_item.keys():
            new_item[key] = val

    with open(Path(__file__).parent.parent/'data'/'user_items.json', 'r') as file:
        file_list = json.load(file)
        file_list.append(new_item)

    with open(Path(__file__).parent.parent/'data'/'user_items.json', 'w') as file:
        json.dump(file_list, file, indent=4)

def removeItem(item_id):
    with open(Path(__file__).parent.parent/'data'/'user_items.json', 'r') as file:
        file_list = json.load(file)
        file_list = [item for item in file_list if item['id']!=item_id]

    with open(Path(__file__).parent.parent/'data'/'user_items.json', 'w') as file:
        json.dump(file_list, file, indent=4)

if __name__ == "__main__":
    resetDatabase()
    addItem({
    "name": "dress for a special occasion",
    "recommendation":"Rent clothes for special occasions.",
    "cathegory": "clothing",
    "score": 80,
    "id": "0001"})
    addItem({
"name": "chain store t-shirt",
"recommendation": "Consider wearing high-quality clothing or buying from second hand.",
"cathegory": "clothing",
"score": 50,
"id": "0002"
})
    removeItem("0002")