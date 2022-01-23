import json

def update_overall_progress(key="", value=""):
    progress = {"name_and_gender": True}
    progress[key] = value
    with open('player_data/player_progress.json', 'w') as f:
        json.dump(progress, f)
    print(f'Wrote {value} in {key}')
    return progress

def check_ai_progress(progress_name):
    player_data_file = open('player_data/player_progress.json')

    progress_data = json.load(player_data_file)
    return progress_data[progress_name]

def check_last_progress():
    player_data_file = open('player_data/player_progress.json')

    progress_data = json.load(player_data_file)
    print(list(progress_data.items())[-1])
    return list(progress_data.items())[-1]

# update_overall_progress()

# print(check_ai_progress("uwu", True))

# ce