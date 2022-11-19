from pathlib import Path
import json
import random

def get_random_item_recommendation():
    with open(Path(__file__).parent.parent/'data'/'recommendations_habits.json', 'r') as file:
        used_recommendations_by_item = json.load(file)
        used_recommendations_by_item = [recomm["item"] for recomm in used_recommendations_by_item]

    with open(Path(__file__).parent.parent/'data'/'items.json', 'r') as file:
        file_list = json.load(file)
        recommendations = [[item['name'], item['recommendation']] for item in file_list
                           if item['recommendation']!="" and item["name"] not in used_recommendations_by_item]

        return recommendations[random.randint(0, len(recommendations)-1)]

def add_goal_from_recommendation(recommendation={}):
    new_recommendation = {"item":None,
                      "recommendation":None}
    new_recommendation["item"] = recommendation[0]
    new_recommendation["recommendation"] = recommendation[1]
    with open(Path(__file__).parent.parent/'data'/'recommendations_habits.json', 'r') as file:
        file_list = json.load(file)
        file_list.append(new_recommendation)

    with open(Path(__file__).parent.parent/'data'/'recommendations_habits.json', 'w') as file:
        json.dump(file_list, file, indent=4)

if __name__ == "__main__":
    # print(get_item_recommendation())
    add_goal_from_recommendation(get_random_item_recommendation())

