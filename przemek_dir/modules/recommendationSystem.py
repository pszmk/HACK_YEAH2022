from pathlib import Path
import json
import random

def getRandomItemRecommendation():
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
        '''some response'''
        pass

def addTransitionGoalFromRecommendation(recommendation={}):
    new_recommendation = {"cathegory":None,
                        "item":None,
                        "recommendation":None}
    new_recommendation["item"] = recommendation[0]
    new_recommendation["recommendation"] = recommendation[1]
    with open(Path(__file__).parent.parent/'data'/'user_recommendations.json', 'r') as file:
        file_list = json.load(file)
        file_list.append(new_recommendation)

    with open(Path(__file__).parent.parent/'data'/'user_recommendations.json', 'w') as file:
        json.dump(file_list, file, indent=4)

if __name__ == "__main__":
    print(getRandomItemRecommendation())