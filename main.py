# College life sim
import json
import os
import random
from reusable import y_n_resp, prcnt_to_grade as prcnt, grade_to_gpa as calc_gpa
from start import start_screen_title, start_new, start_new_or_load, intro
from data import fem_names, masc_names, gend_neut_names as nb_names, surnames

seasons_dict = {1: 'Autumn', 2: 'Winter', 3: 'Spring', 4: 'Summer'}
grade_levels_dict = {1: 'Freshman', 2: 'Sophomore', 3: 'Junior', 4: 'Senior'}
locations_list = ['Auditorium', 'Bar', 'Basketball Court', 'Bookstore', 'Cafeteria', 'Classroom', 'Clothing store', 'Club', 'Dorms', 'Football Field', 'Grocery Store', 'Gym', 'Hallway', 'Library', 'Lab', 'Laundry Room', 'Restaurant', 'Stadium', 'Stairwell', 'Student Central', 'Quad']
# majors = ['Architecture', 'Art', 'Biology', 'Business', 'Chemistry', 'Computer Science', 'Criminology', 'Education', 'Economics', 'Engineering', 'Health', 'History', 'Mathematics', 'Sociology', 'Writing']
npc_list = []
npc_dict = []

class School:
  fem = 0
  masc = 0
  nb = 0
  actions = 0
  name = 'Oxbridge University'
  season = seasons_dict[1]
  day = 1

  def __init__(self):
    pass

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
    self.personality_traits = {'conscientiousness': 0, 'agreeableness': 0, 'neuroticism': 0, 'openness to experience': 0, 'extraversion': 0}

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
  gender: 'fem', 'masc', or 'nb'
  npc_info: dictionary to hold each npc's information
          --> {'name': string, 'gender': string, 'friendship': int, 'romance': int, 'personality': {'conscientiousness': 7, 'agreeableness': 3, ...}}
  friendship: level of friendship with player
          --> -100 - 100
  romance: level of romance with player
          --> 0 - 100
  chooseName(): randomizes gender and chooses name based on their gender
  create_personality(): randomizes how many points are put into each big personality trait
  choose_response(): chooses the type of response the character gives in any given situation based on the friendship level
  choose_romantic_response(): chooses a romantic response based on the romance level, if there's any romance higher than 0
  add_to_dict(): add the npc's info to the npc dictionary
'''
class NpcStudent(Student):
  def __init__(self):
    super().__init__()
    self.gender = ''
    coin_flip = random.randint(1, 3)
    if coin_flip == 1 and School.fem < 5 or School.masc == 5 and School.fem < 5 or School.nb == 5 and School.fem < 5: self.gender = 'fem'; School.fem += 1
    elif coin_flip == 2 and School.masc < 5 or School.fem == 5 and School.masc < 5 or School.nb == 5 and School.masc < 5: self.gender = 'masc'; School.masc += 1
    elif coin_flip == 3 and School.nb < 5 or School.fem == 5 and School.nb < 5 or School.masc == 5 and School.enby < 5: self.gender = 'nb'; School.nb += 1
    npc_list.append(self)
    self.npc_info = {}
    self.friendship = 0
    self.romance = 0
  
  def choose_name(self):
    rand_last = random.randint(0, len(surnames))
    if self.gender == 'fem':
      rand_first = random.randint(0, len(fem_names))
      if fem_names[rand_first] in surnames[rand_last] or surnames[rand_last] in fem_names[rand_first]:
        if rand_last == len(surnames) - 1: self.name = fem_names[rand_first] + ' ' + surnames[rand_last - 1]
        else: self.name = fem_names[rand_first] + ' ' + surnames[rand_last + 1]
      else: self.name = fem_names[rand_first] + ' '  + surnames[rand_last]
    elif self.gender == 'masc':
      rand_first = random.randint(0, len(masc_names))
      if masc_names[rand_first] in surnames[rand_last] or surnames[rand_last] in masc_names[rand_first]:
        if rand_last == len(surnames) - 1: self.name = masc_names[rand_first] + ' ' + surnames[rand_last - 1]
        else: self.name = masc_names[rand_first] + ' ' + surnames[rand_last + 1]
      else: self.name = masc_names[rand_first] + ' ' + surnames[rand_last]
    elif self.gender == 'nb':
      rand_first = random.randint(0, len(nb_names))
      if nb_names[rand_first] in surnames[rand_last] or surnames[rand_last] in nb_names[rand_first]:
        if rand_last == len(surnames) - 1: self.name = nb_names[rand_first] + ' ' + surnames[rand_last - 1]
        else: self.name = nb_names[rand_first] + ' ' + surnames[rand_last + 1]
      else: self.name = nb_names[rand_first] + ' ' + surnames[rand_last]
    self.npc_info['name'] = self.name
    self.npc_info['gender'] = self.gender
    self.npc_info['friendship'] = self.friendship
    self.npc_info['romance'] = self.romance

  def create_personality(self):
    points_allocated = 0
    while points_allocated <= 23:
      bigFive = random.randint(1, 5)
      if bigFive == 1:
        self.personality_traits['conscientiousness'] += 1
        points_allocated += 1
      if bigFive == 2:
        self.personality_traits['agreeableness'] += 1
        points_allocated += 1
      if bigFive == 3:
        self.personality_traits['neuroticism'] += 1
        points_allocated += 1
      if bigFive == 4:
        self.personality_traits['openness to experience'] += 1
        points_allocated += 1
      if bigFive == 5:
        self.personality_traits['extraversion'] += 1
        points_allocated += 1
    self.npc_info['personality'] = self.personality_traits
    print(self.npc_info)
      

  def choose_response(self):
    if self.romance >= 1:
      self.chooseRomanticResponse()
    if self.friendship >= 0 and self.friendship <= 30:
      response = 'neutral'
      return response
    elif self.friendship >= 31 and self.friendship <= 60:
      response = 'friendly'
      return response
    elif self.friendship >= 61 and self.friendship <= 100:
      response = 'warmhearted'
      return response
    elif self.friendship <= -1 and self.friendship >= -30:
      response = 'distant'
      return response
    elif self.friendship <= -31 and self.friendship >= -60:
      response = 'antagonistic'
      return response
    elif self.friendship <= -61 and self.friendship >= -100:
      response = 'hostile'
      return response

  def choose_romantic_response(self):
    if self.romance >= 1 and self.romance <= 30:
      response = 'flattered'
      return response
    elif self.romance >= 31 and self.romance <= 60:
      response = 'flirtatious'
      return response
    elif self.romance >= 61 and self.romance <= 100:
      response = 'loving'
      return response
  
  def add_to_dict(self):
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
npc11 = NpcStudent()
npc12 = NpcStudent()
npc13 = NpcStudent()
npc14 = NpcStudent()
npc15 = NpcStudent()
for npc in npc_list:
  npc.choose_name()
  npc.create_personality()
  npc.add_to_dict()
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