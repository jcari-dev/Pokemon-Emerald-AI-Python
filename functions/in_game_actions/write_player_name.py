import time
import itertools


def get_movement_for_character(index_list):
    starting_point = [0, 0]
    caps = True
    lower = False
    symbols = False
    command_list = []

    for index, character_indexes in enumerate(index_list):
        x_axis, y_axis = character_indexes[0], character_indexes[1]

        if y_axis >= 8:
            starting_point[1] += 8
            if starting_point[1] >= 10:
                starting_point[1] -= 4
            if caps == True:
                command_list.append('backspace')
                command_list.append('backspace')
                lower = False
                symbols = True
                caps = False
            elif lower == True:
                command_list.append('backspace')
                lower = False
                symbols = True
                caps = False
        elif y_axis >= 4:
            # print(starting_point)
            starting_point[1] += 4
            if starting_point[1] >= 8:
                # print(starting_point[1])
                if starting_point[1] >= 10:
                    starting_point[1] -= 4
                starting_point[1] -= 4
            if caps == True:
                command_list.append('backspace')
                lower = True
                symbols = False
                caps = False
            elif symbols == True:
                command_list.append('backspace')
                command_list.append('backspace')
                lower = True
                symbols = False
                caps = False
        elif y_axis <= 4 and symbols == True:
            command_list.append('backspace')
            lower = False
            symbols = False
            caps = True
            # print(y_axis, starting_point, 'got the 1?')
            starting_point[1] = 0
            # print(starting_point[1])

        # print(x_axis, y_axis)


        x_diff, y_diff = x_axis - starting_point[0], starting_point[1] - y_axis



        if x_diff < 0:
            for diff in range(abs(x_diff)):
                command_list.append('left')
        elif x_diff > 0:
            for diff in range(x_diff):
                command_list.append('right')

        if y_diff < 0:
            for diff in range(abs(y_diff)):
                command_list.append("down")
        elif y_diff > 0:
            for diff in range(y_diff):
                command_list.append('up')
        command_list.append('x')
        starting_point = character_indexes
    command_list.append('enter')
    command_list.append('x')
    command_list.append('x')
    return command_list


def get_index_of_characters(name):

    character_list = (
        ("A", "B", "C", "D", "E", "F", " ", "."),
        ("G", "H", "I", "J", "K", "L", " ", ","),
        ("M", "N", "O", "P", "Q", "R", "S", " "),
        ("T", "U", "V", "W", "X", "Y", "Z", " "),
        ("a", "b", "c", "d", "e", "f", " ", "."),
        ("g", "h", "i", "j", "k", "l", " ", ","),
        ("m", "n", "o", "p", "q", "r", "s", " "),
        ("t", "u", "v", "w", "x", "y", "z", " "),
        ("0", "1", "2", "3", "4", " "),
        ("5", "6", "7", "8", "9", " "),
        ("!", "?", " ", " ", "/", "-"),
    )

    # print(character_list[8][0])
    index_locations = []

    for index_name, name_character in enumerate(name):
        for index_array, array in enumerate(character_list):
            for index_inner, inner_character in enumerate(array):
                if name_character == inner_character:
                    index_locations.append([index_inner, index_array])

    # print(index_locations)

    return get_movement_for_character(index_locations)
    # return index_locations


# print(get_index_of_characters('Ines'))
