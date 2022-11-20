from pathlib import Path
import json

def getFoods(names=True):
    with open(Path(__file__).parent.parent/'data'/'user_items.json', 'r') as file:
        file_list = json.load(file)
        file_list = [item for item in file_list if item['cathegory']=='food']
    if names:
        return [item["name"] for item in file_list]
    return file_list

def getRecepies():
    items = getFoods()
    with open(Path(__file__).parent.parent/'data'/'all_recepies.json', 'r') as file:
        file_list = json.load(file)
        # print(file_list)
        # print(list(sorted(file_list, key=lambda x: sum([item in x['key_ingredients'] for item in items]),reverse=True)))
        #
        # x = list(sorted(file_list, key=lambda x: sum([item in x['key_ingredients'] for item in items]), reverse=True))
        # print([item['key_ingredients'] for item in x])
        # print(file_list)
        # x['key_ingredients']
        # for x in file_list
        # print([item in x['key_ingredients'] for item in items for x in file_list])
        # return list(sorted(file_list, key=lambda x: sum([item in x['key_ingredients'] for item in items]), reverse=True))
    # print(file_list)
    # for litem in file_list:
        # print(litem['key_ingredients'])
        # for item in items:
        #     print([item in ['key_ingredients']])



def planShoppinglist():
    pass

if __name__ == "__main__":
    from przemek_dir.modules.jsonDatabase import addItem, resetDatabase

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
    # print(getFoods())
    # # print(len(getFoods()))
    # print([food['name'] for food in getFoods()])
    resetDatabase()
    # with open(Path(__file__).parent.parent/'data'/'all_possible_items.json', 'r') as file:
    #     file_list = json.load(file)
    #     file_list = [item['name'] for item in file_list['food']]
    #     print(*file_list)
    getRecepies()