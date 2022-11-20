from pathlib import Path
import json
import random

def getRandomItemRecommendation():
    '''Returns random recommendation based on the possesed items from the items recommendations.
    '''
    with open(Path(__file__).parent.parent/'data'/'user_recommendations.json', 'r') as file:
        user_recommendations_by_item = json.load(file)['item_recommendations']
        user_recommendations_by_item = [recomm["item"] for recomm in user_recommendations_by_item]

    with open(Path(__file__).parent.parent/'data'/'user_items.json', 'r') as file:
        file_list = json.load(file)
        recommendations = [[item['cathegory'], item['name'], item['recommendation']] for item in file_list
                           if item['recommendation']!="" and item["name"] not in user_recommendations_by_item]

    if len(recommendations):
        return recommendations[random.randint(0, len(recommendations)-1)]
    else:
        return []

def addTransitionGoalFromRecommendation(recommendation={}):
    '''Add new goal based on the item recommendation to the file user_recommendations.json.
    '''
    new_recommendation = {"cathegory":None,
                        "item":None,
                        "recommendation":None}
    new_recommendation["item"] = recommendation[0]
    new_recommendation["recommendation"] = recommendation[1]
    with open(Path(__file__).parent.parent/'data'/'user_recommendations.json', 'r') as file:
        file_list = json.load(file)
        file_list['item_recommendations'].append(new_recommendation)

    with open(Path(__file__).parent.parent/'data'/'user_recommendations.json', 'w') as file:
        json.dump(file_list, file, indent=4)

def resetRecommendations():
    with open(Path(__file__).parent.parent/'data'/'user_recommendations.json', 'w') as file:
        json.dump({"item_recommendations": [],
                    "habit_recommendations": []},
                  file, indent=4)

if __name__ == "__main__":
    from przemek_dir.modules.jsonDatabase import addItem, resetDatabase
    resetDatabase()
    addItem({
        "name": "onion",
        "recommendation":"",
        "cathegory": "food",
        "score": 90
        })
    addItem({
        "name": "lupinus",
        "recommendation":"",
        "cathegory": "food",
        "score": 90
        })
    addItem({
        "name": "soybeans",
        "recommendation":"Consider eatin pulses instead. Soybeams require a lot of water to grow.",
        "cathegory": "food",
        "score": 20
        })
    addItem({
        "name": "fish",
        "recommendation":"Consider eating pulses instead. Popular fish are geting overfished.",
        "cathegory": "food",
        "score": 30
        })
    addItem({
        "name": "rice",
        "recommendation":"Consider replaceing it with potatoes. Rice require a lot of water to grow.",
        "cathegory": "food",
        "score": 20
        })

    print(getRandomItemRecommendation())
    resetRecommendations()
    addTransitionGoalFromRecommendation(getRandomItemRecommendation())
    resetDatabase()
