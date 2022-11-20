from pathlib import Path
import json

def getFoods(names=True):
    '''Return food stored by the user.
    '''
    with open(Path(__file__).parent.parent/'data'/'user_items.json', 'r') as file:
        file_list = json.load(file)
        file_list = [item for item in file_list if item['cathegory']=='food']
    if names:
        return [item["name"] for item in file_list]
    return file_list

def getRecepies():
    '''Return recepies in the order defined by the current state of the user's food inventory.
    The recepies consist of the title, indegreients the steps.
    '''
    items = getFoods()
    with open(Path(__file__).parent.parent/'data'/'all_recepies.json', 'r') as file:
        file_list = json.load(file)
        return list(sorted(file_list, key=lambda x: sum([item in x['key_ingredients'] for item in items]), reverse=True))

def planShoppinglist():
    pass

if __name__ == "__main__":
    from python_part.modules.jsonDatabase import addItem, resetDatabase
    resetDatabase()
    addItem({
        "name": "rice",
        "recommendation": "Consider replaceing it with potatoes. Rice require a lot of water to grow.",
        "cathegory": "food",
        "score": 20
    })
    addItem({
        "name": "organic shampoo in reusable bottle",
        "recommendation":"",
        "cathegory": "hygiene",
        "score": 100
    })
    addItem({
        "name": "potato",
        "recommendation": "",
        "cathegory": "food",
        "score": 80
    })
    addItem({
        "name": "organic shampoo in reusable bottle",
        "recommendation":"",
        "cathegory": "hygiene",
        "score": 100
        })
    print(getRecepies())
    resetDatabase()