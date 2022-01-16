# import timeit
import itertools
# def get_actions_to_write_1(name):

#     character_list = [
#     ['A', 'B', 'C', 'D', 'E', 'F', ' ', '.'],
#     ['G', 'H', 'I', 'J', 'K', 'L', ' ', ','],
#     ['M', 'N', 'O', 'P', 'Q', 'R', 'S', ' '],
#     ['T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' '],
#     ['a', 'b', 'c', 'd', 'e', 'f', ' ', '.'],
#     ['g', 'h', 'i', 'j', 'k', 'l', ' ', ','],
#     ['m', 'n', 'o', 'p', 'q', 'r', 's', ' '],
#     ['t', 'u', 'v', 'w', 'x', 'y', 'z', ' '],
#     ['0', '1', '2', '3', '4', ' '],
#     ['5', '6', '7', '8', '9', ' '],
#     ['!', '?', '+', '+', '/', '-']]
    
#     for index_name, name_character in enumerate(name):
#         for index_array, array in enumerate(character_list):
#             for index_inner, inner_character in enumerate(array):
#                 if name_character == inner_character:
#                   return index_array, index_inner
                  
# def get_actions_to_write_2(name):

#     character_list = (
#     ('A', 'B', 'C', 'D', 'E', 'F', ' ', '.'),
#     ('G', 'H', 'I', 'J', 'K', 'L', ' ', ','),
#     ('M', 'N', 'O', 'P', 'Q', 'R', 'S', ' '),
#     ('T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' '),
#     ('a', 'b', 'c', 'd', 'e', 'f', ' ', '.'),
#     ('g', 'h', 'i', 'j', 'k', 'l', ' ', ','),
#     ('m', 'n', 'o', 'p', 'q', 'r', 's', ' '),
#     ('t', 'u', 'v', 'w', 'x', 'y', 'z', ' '),
#     ('0', '1', '2', '3', '4', ' '),
#     ('5', '6', '7', '8', '9', ' '),
#     ('!', '?', '+', '+', '/', '-'))
    
    
#     for index_name, name_character in enumerate(name):
#         for index_array, array in enumerate(character_list):
#             for index_inner, inner_character in enumerate(array):
#                 if name_character == inner_character:
#                   print(index_array, index_inner)


# # get_actions_to_write_1('Juan')
# # get_actions_to_write_2('Juan')

# timeit.timeit(lambda: get_actions_to_write_1('Juan'))

def get_movement_order(index_locations):
  old_location = [0,0]
  beginning = [0,0]
  letter_sequence = []
  all_caps = True
  all_lower = False
  numbers = False
  
  r = 'right'
  l = 'left'
  u = 'up'
  d = 'down'


  for index, location in enumerate(index_locations):
    if location[0] > beginning[0]:
      if location[0] >= 4:
        if all_lower == False:
          all_lower = True
          all_caps = False
          numbers = False
          location[0] -=4
          letter_sequence.append(['backspace'])
        else:
          print('skipped backspace because we aleady in lower case')
      elif location[0] >= 8:
        numbers = True
        all_caps = False
        all_lower = False
        old_location[0] = location[0]
        location[0] -=8
        letter_sequence.append(['backspace'])

      move_right = abs(beginning[0] - location[0])
      rs = ["down" for x in range(move_right)]
      # rs.append('x')
      letter_sequence.append(rs)
      old_location[0] = location[0]


      # print(letter_sequence)
    else:
      if location[0] >= 4:
        if all_lower == False:
          all_lower = True
          all_caps = False
          numbers = False
          location[0] -=4
          letter_sequence.append(['backspace'])
        else:
          print('skipped backspace because we already in lower case')
      elif location[0] >= 8:
        location[0] -= 8
        letter_sequence.append(['backspace'])
      move_left = abs(beginning[1] - location[0])
      ls = ["up" for x in range(move_left)]
      # ls.append('x')
      letter_sequence.append(ls)
      old_location[0] = location[0]
      # print(letter_sequence)

    if location[1] > beginning[1]:

      if location[1] >= 4:
        if all_lower == False:
          all_lower = True
          all_caps = False
          numbers = False
          location[1] -=4
          letter_sequence.append(['backspace'])
        else:
          print('skipped backspace because we already in lower case')
      elif location[1] >= 8:

        location[1] -= 8
        letter_sequence.append(['backspace'])
      move_up = abs(beginning[1] - location[1])
      us = ['right' for x in range(move_up)]
      # us.append('x')
      letter_sequence.append(us)
      old_location[1] = location[1]
      # print(letter_sequence)
    else:
      if location[1] >= 4:
        if all_lower == False:
          all_lower = True
          all_caps = False
          numbers = False
          location[1] -=4
          letter_sequence.append(['backspace'])
        else:
          print('skipped backspace because we already in lower case')
      elif location[1] >= 8:
        location[1] -=8
        letter_sequence.append(['backspace'])
      move_down = abs(beginning[1] - location[1])
      ds = ['left' for x in range(move_down)]
      # ds.append('x')
      letter_sequence.append(ds)
      old_location[1] = location[1]
      # print(letter_sequence)
    beginning = old_location
    
    letter_sequence.append('x')
  print(old_location)
  flatted_sequence = list(itertools.chain(*letter_sequence))
  print(flatted_sequence)
  print(len(flatted_sequence))

def get_index_of_characters(name):

  character_list = (
    ('A', 'B', 'C', 'D', 'E', 'F', '+', '.'),
    ('G', 'H', 'I', 'J', 'K', 'L', '+', ','),
    ('M', 'N', 'O', 'P', 'Q', 'R', 'S', '+'),
    ('T', 'U', 'V', 'W', 'X', 'Y', 'Z', '+'),
    ('a', 'b', 'c', 'd', 'e', 'f', '+', '.'),
    ('g', 'h', 'i', 'j', 'k', 'l', '+', ','),
    ('m', 'n', 'o', 'p', 'q', 'r', 's', '+'),
    ('t', 'u', 'v', 'w', 'x', 'y', 'z', '+'),
    ('0', '1', '2', '3', '4', '+'),
    ('5', '6', '7', '8', '9', '+'),
    ('!', '?', '+', '+', '/', '-'))
  print(character_list[8][0])
  index_locations = []
    
  for index_name, name_character in enumerate(name):
      for index_array, array in enumerate(character_list):
          for index_inner, inner_character in enumerate(array):
              if name_character == inner_character:
                index_locations.append([index_array, index_inner])

  print(index_locations)
  get_movement_order(index_locations)

  return index_locations


get_index_of_characters('Jennie')