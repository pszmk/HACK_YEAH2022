from pathlib import Path
import json

def resetScore():
    with open(Path(__file__).parent.parent / 'data' / 'user_score.json', 'w') as file:
        json.dump({"score": 0,"combo": 1}, file, indent=4)


def add_subScore(score=0, add=True):
    with open(Path(__file__).parent.parent/'data'/'user_score.json', 'r') as file:
        file_list = json.load(file)
        if add:
            file_list["score"] += score*file_list['combo']
        else:
            file_list["score"] -= score * file_list['combo']
    with open(Path(__file__).parent.parent / 'data' / 'user_score.json', 'w') as file:
        json.dump(file_list, file, indent=4)

if __name__ == "__main__":
    add_subScore(3)
    resetScore()