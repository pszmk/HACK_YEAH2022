from pathlib import Path
import json

def add_item(item={}):
    new_item = {
        "name": None,
        "recommendation": None,
        "cathegory": None,
        "score": None
        }

    for key, val in item.items():
        if key in new_item.keys():
            new_item[key] = val

    with open(Path(__file__).parent.parent/'data'/'items.json', 'r') as file:
        file_list = json.load(file)
        file_list.append(new_item)

    with open(Path(__file__).parent.parent/'data'/'items.json', 'w') as file:
        json.dump(file_list, file, indent=4)

def add_routine():
    pass

if __name__ == "__main__":
    add_item({
    "name": "dress for a special occasion",
    "recommendation":"Rent clothes for special occasions.",
    "cathegory": "clothing",
    "score": 80})
    add_item({
"name": "chain store t-shirt",
"recommendation": "Consider wearing high-quality clothing or buying from second hand.",
"cathegory": "clothing",
"score": 50
})

    # print(Path(__file__).parent.parent/'data')