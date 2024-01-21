# College life sim
import json
import os
import random
from reusable import y_n_resp, prcnt_to_grade as prcnt, grade_to_gpa as calc_gpa
from start import start_screen_title, start_new, start_new_or_load, intro
from data import fem_names, masc_names, surnames

seasons_dict = {1: 'Autumn', 2: 'Winter', 3: 'Spring', 4: 'Summer'}
grade_levels_dict = {1: 'Freshman', 2: 'Sophomore', 3: 'Junior', 4: 'Senior'}
locations_list = ['Auditorium', 'Bar', 'Basketball Court', 'Bookstore', 'Cafeteria', 'Classroom', 'Clothing store', 'Club', 'Dorms', 'Football Field', 'Grocery Store', 'Gym', 'Hallway', 'Library', 'Lab', 'Laundry Room', 'Restaurant', 'Stadium', 'Stairwell', 'Student Central', 'Quad']
# majors = ['Architecture', 'Art', 'Biology', 'Business', 'Chemistry', 'Computer Science', 'Criminology', 'Education', 'Economics', 'Engineering', 'Health', 'History', 'Mathematics', 'Sociology', 'Writing']
npc_list = []
npc_dict = []

class School:
  fem = 0
  masc = 0
  actions = 0
  name = 'Oxbridge University'
  season = seasons_dict[1]
  day = 1

  def __init__(self):
    students = []

  def changeDay(self):
    if School.actions >= 6:
      School.day += 1
      if School.day == 4 and School.season == seasons_dict[4]:
        School.season = seasons_dict[1]
        School.day = 1
      elif School.day == 4:
        for num in range(1, 4):
          School.day = 1
          if School.season == seasons_dict[num]:
            School.season = seasons_dict[num + 1]
            break
      School.actions = 0
        

class Location:
  def __init__(self):
    pass

# Base class for all students
  '''
  ╭ ------------------------ ╮
  *    Student Attributes    *
  ╰ ------------------------ ╯
  name: string
  personality_traits: dictionary of where they fall on the Big Five personality traits 0-10 (conscientiousness, agreeableness, neuroticism, openness to experience, extraversion)
          --> {'conscientiousness': 7, 'agreeableness': 3, ...}
  '''
class Student:
  def __init__(self):
    self.name = ''
    self.personality_traits = {}

  def calculateGPA(self):
    for value in self.courses.values():
      self.gpa += calc_gpa[value]
    self.gpa = self.gpa/len(self.courses)

# Class for player
'''
  ╭ ----------------------- ╮
  *    Player Attributes    *
  ╰ ----------------------- ╯
  gpa: float
  courses: dictionary formatted with each course as the key and the grade as value 
          --> {'English': B-}
  friends: dictionary formatted with the friend's name as the key and the friendship level as the value 
          --> {'friend1 name': 50, ...}
  enemies: dictionary formatted the same as friends, but will be anything less than 0 
          --> {'enemy1 name': -20, ...}
  romantic_interest: list of dictionaries formatted with name of NPC's name key with interest level value, a status of bf/gf key &a boolean value 
          --> [{'love interest name': 45, 'bf/gf': False}, ...]
'''
class Player(Student):
  def __init__(self):
    super().__init__()
    self.gpa = 0
    self.courses = {}
    self.friends = {}
    self.enemies = {}
    self.romantic_interest = {}
    

# Class for NPCs
'''
  ╭ -------------------- ╮
  *    NPC Attributes    *
  ╰ -------------------- ╯
  fem: boolean
      True for feminine NPC, False for masculine NPC
'''
class NpcStudent(Student):
  def __init__(self):
    super().__init__()
    coin_flip = random.randint(1, 2)
    if coin_flip == 1 and School.fem < 5 or School.masc == 5 and School.fem < 5: self.fem = True; School.fem += 1
    elif coin_flip == 2 and School.masc < 5 or School.fem == 5 and School.masc < 5: self.fem = False; School.masc += 1
    npc_list.append(self)
    self.npc_info = {}
    self.friendship = 0
    self.romance = 0
  
  def choose_name(self):
    if self.fem == True:
      rand_first = random.randint(0, len(fem_names))
      rand_last = random.randint(0, len(surnames))
      if fem_names[rand_first] in surnames[rand_last] or surnames[rand_last] in fem_names[rand_first]:
        if surnames[rand_last] == len(surnames) - 1: self.name = fem_names[rand_first] + ' ' + surnames[rand_last - 1]
        else: self.name = fem_names[rand_first] + ' ' + surnames[rand_last + 1]
      else: self.name = fem_names[rand_first] + ' '  + surnames[rand_last]
      print('FEM:' + ' ' + self.name)
    else:
      rand_first = random.randint(0, len(masc_names))
      rand_last = random.randint(0, len(surnames))
      if masc_names[rand_first] in surnames[rand_last] or surnames[rand_last] in masc_names[rand_first]:
        if surnames[rand_last] == len(surnames) - 1: self.name = masc_names[rand_first] + ' ' + surnames[rand_last - 1]
        else: self.name = masc_names[rand_first] + ' ' + surnames[rand_last + 1]
      else: self.name = masc_names[rand_first] + ' ' + surnames[rand_last]
      print('MASC:' + ' ' + self.name)
    self.npc_info['fem'] = self.fem
    self.npc_info['name'] = self.name
    self.npc_info['friendship'] = self.friendship
    self.npc_info['romance'] = self.romance
    npc_dict.append(self.npc_info)
    

player = Player()
player.name = 'Brielle'
print(player.name)
npc1 = NpcStudent()
npc2 = NpcStudent()
npc3 = NpcStudent()
npc4 = NpcStudent()
npc5 = NpcStudent()
npc6 = NpcStudent()
npc7 = NpcStudent()
npc8 = NpcStudent()
npc9 = NpcStudent()
npc10 = NpcStudent()
for npc in npc_list:
  npc.choose_name()
print(f'''
FEM: {School.fem}
MASC: {School.masc}
''')
print(npc_dict)





# def load_save(player:Player):
#   with open('save_file.json', 'r') as save:
#     data = json.load(save)
#     player.name = data['player.name']
#     School.season = data['School.season']
#     School.day = data['School.day']
    

# def create_player(player:Player):
#   confirmed = False
#   redo = False
#   while not confirmed:
#     if redo == True:
#       player_name = input('I\'m sorry about that, please enter your name again.\n>>> ')
#     else: 
#       player_name = input('Hi, and welcome to your first day at Oxbridge University! What\'s your name?\n>>> ')
#     while True:
#       confirm = input(f'I have you down as {player_name}. Is that correct?\n(y/n)>>> ')
#       if confirm in y_n_resp:
#         if confirm == 'y':
#           player.name = player_name
#           print(f'Welcome, {player.name}!')
#           confirmed = True
#           break
#         elif confirm == 'n':
#           redo = True
#           break
#       print('That\'s an invalid input, please try again.')

#   player.name = player_name

#   save_data = {
#     'player_name': player.name,
#     'School_season': School.season,
#     'School_day': School.day
#   }

#   with open('save_file.json', 'w') as save:
#     json.dump(save_data, save)

# def launch():
#   if os.path.exists('save_file.json') == True:
#     player = Player('')
#     print(
#       start_screen_title,
#       start_new_or_load
#     )
#     start_input = ''
#     confirmed = False
#     while not confirmed:
#       while True:
#         start_input = input('Type \'1\' and press enter to start a new story at Oxbridge University\nor type \'2\' to continue your previous story.\n>>> ')
#         if start_input == '1':
#           while True:
#             confirm = input('Please confirm that you want to START OVER\n(y/n)>>> ')
#             if confirm in y_n_resp:
#               if confirm == 'y':
#                 os.remove('save_file.json')
#                 confirmed = True
#                 create_player(player)
#                 break
#               elif confirm == 'n':
#                 break
#               print('That\'s an invalid input, please try again.')
#           break
#         elif start_input == '2':
#           while True:
#             confirm = input('Please confirm that you want to LOAD SAVE\n(y/n)>>> ')
#             if confirm in y_n_resp:
#               if confirm == 'y':
#                 confirmed = True
#                 load_save(player)
#                 break
#               elif confirm == 'n':
#                 break
#             print('That\'s an invalid input, please try again.')
#           break
#         print('That\'s an invalid input, please try again.')
#   else:
#     player = Player('')
#     print(
#       start_screen_title,
#       start_new,
#       intro
#     )
#     start_input = None
#     while True:
#       start_input = input('Type \'1\' and press enter to start your life at Oxbridge University!\n>>> ')
#       if start_input == '1':
#         create_player(player)
#         break
#       print('That\'s an invalid input, please try again.')

# if __name__ == "__main__":
#   launch()