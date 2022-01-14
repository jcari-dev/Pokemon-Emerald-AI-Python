import json


def write_player_data(player_data):

    data = player_data
    with open('player_data/playing_data.json', 'w') as f:
        json.dump(data, f)