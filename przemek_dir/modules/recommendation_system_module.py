from pathlib import Path
import json
import random

def get_random_item_recommendation():
    with open(Path(__file__).parent.parent/'data'/'user_recommendations_habits.json', 'r') as file:
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

def get_random_cathegoryspecific_recommendation(cat=None):
    with open(Path(__file__).parent.parent/'data'/'all_cathegoryspecific_recommendations.json', 'r') as file:
        all_cat_recom = json.load(file)['']

    if cat == 'clothing':
        if len(all_cat_recom['clothing']):
            with open(Path(__file__).parent.parent / 'data' / 'user_recommendations_habits.json', 'r') as file:
                file_list = json.load(file)['habit_recommendations']
            file_list = [one_recom['recommendation'] for one_recom in file_list]
            all_cat_recom = [recom for recom in all_cat_recom['clothing'] if recom['recommendation'] not in file_list]
            return all_cat_recom['clothing'][random(0, len(all_cat_recom['clothing'])-1)]
        else:
            return []
    elif cat == 'food':
        if len(all_cat_recom['food']):
            with open(Path(__file__).parent.parent / 'data' / 'user_recommendations_habits.json', 'r') as file:
                file_list = json.load(file)
            file_list = [one_recom['recommendation'] for one_recom in file_list]
            all_cat_recom = [recom for recom in all_cat_recom['food'] if recom['recommendation'] not in file_list]
            return all_cat_recom['food'][random(0, len(all_cat_recom['food']) - 1)]
        else:
            return []
    elif cat == 'hygiene':
        if len(all_cat_recom['hygiene']):
            with open(Path(__file__).parent.parent / 'data' / 'user_recommendations_habits.json', 'r') as file:
                file_list = json.load(file)
            file_list = [one_recom['recommendation'] for one_recom in file_list]
            all_cat_recom = [recom for recom in all_cat_recom['clothing'] if recom['recommendation'] not in file_list]
            return all_cat_recom['hygiene'][random(0, len(all_cat_recom['hygiene']) - 1)]
        else:
            return []
    else:
        pass

def add_goal_from_recommendation(recommendation={}):
    new_recommendation = {"cathegory":None,
                        "item":None,
                        "recommendation":None}
    new_recommendation["item"] = recommendation[0]
    new_recommendation["recommendation"] = recommendation[1]
    with open(Path(__file__).parent.parent/'data'/'user_recommendations_habits.json', 'r') as file:
        file_list = json.load(file)
        file_list.append(new_recommendation)

    with open(Path(__file__).parent.parent/'data'/'user_recommendations_habits.json', 'w') as file:
        json.dump(file_list, file, indent=4)

if __name__ == "__main__":
    # get_random_item_recommendation()
    # print(get_random_item_recommendation())
    print(get_random_cathegoryspecific_recommendation(cat='food'))
    # add_goal_from_recommendation(get_random_item_recommendation())
    # with open(Path(__file__).parent.parent/'data'/'all_cathegoryspecific_recommendations.json', 'r') as file:
    #     all_cat_recom = json.load(file)
    #     print(all_cat_recom)
