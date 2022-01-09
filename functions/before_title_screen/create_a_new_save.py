import os

def create_new_save():
    print('\033[92m' + "Welcome to JC's Pokemon Emerald Bot!" + '\033[0m')
    print("\n======================================================= \nPlease be sure to answer these questions! If you want a random value for each response just press leave them empty! \n=======================================================")
    player_name = input("What is your name? We currently support [A-z], [0-9], [,.!?/-\"] Maximum 7 characters, e.g. Leg3n-d, cool right? \nI can also give you a name myself (not implemented yet, but soon!) just type 'nameMe': ")
    player_gender = input("Are you a boy or a girl? (The game literally needs to know this!) (boy/girl): ")
    player_starter_pokemon = input("Select your starter Pokemon Treecko, Torchic, or Mudkip? (1,2,3): ")
    real_time_clock = input("Do you want to use your device's time? (Y/N): ")
