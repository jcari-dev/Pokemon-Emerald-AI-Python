from images.comparasion_script.perform_action import perform

def change_text_speed_to_fast():
    actions = ['down', 'right', 'c', 'up']
    
    perform(actions[0])
    perform(actions[1])
    perform(actions[2])
    perform(actions[3])