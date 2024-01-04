# College life sim
import json
import os
from reusable import y_n_resp
from start import start_screen_title, start_new, start_new_or_load, intro

seasons_dict = {1: 'Autumn', 2: 'Winter', 3: 'Spring', 4: 'Summer'}
grade_levels_dict = {1: 'Freshman', 2: 'Sophomore', 3: 'Junior', 4: 'Senior'}
locations_list = ['Auditorium', 'Bar', 'Basketball Court', 'Bookstore', 'Cafeteria', 'Classroom', 'Clothing store', 'Club', 'Dorms', 'Football Field', 'Grocery Store', 'Gym', 'Hallway', 'Library', 'Lab', 'Laundry Room', 'Restaurant', 'Stadium', 'Stairwell', 'Quad']
majors = ['Architecture', 'Art', 'Biology', 'Business', 'Chemistry', 'Computer Science', 'Criminology', 'Education', 'Economics', 'Engineering', 'Health', 'History', 'Mathematics', 'Sociology', 'Writing']

class School:
  season = seasons_dict[1]
  day = 1
  def __init__(self, school_name):
    self.name = school_name

class Location:
  def __init__(self):
    pass

class Student:
  def __init__(self):
    self.name = ''

class Player:
  def __init__(self, name):
    self.name = name

def load_save(player:Player):
  with open('save_file.json', 'r') as save:
    data = json.load(save)
    print(data)

def create_player(player:Player):
  confirmed = False
  redo = False
  while not confirmed:
    if redo == True:
      player_name = input('I\'m sorry about that, please enter your name again.\n>>> ')
    else: 
      player_name = input('Hi, and welcome to your first day at Oxbridge University! What\'s your name?\n>>> ')
    while True:
      confirm = input(f'I have you down as {player_name}. Is that correct?\n(y/n)>>> ')
      if confirm in y_n_resp:
        if confirm == 'y':
          player.name = player_name
          print(f'Welcome, {player.name}!')
          confirmed = True
          break
        elif confirm == 'n':
          redo = True
          break
      print('That\'s an invalid input, please try again.')

  player.name = player_name

  save_data = {
    'player.name': player.name,
    'School.season': School.season,
    'School.day': School.day
  }

  with open('save_file.json', 'w') as save:
    json.dump(save_data, save)

def launch():
  if os.path.exists('save_file.json') == True:
    player = Player('')
    print(
      start_screen_title,
      start_new_or_load
    )
    start_input = ''
    confirmed = False
    while not confirmed:
      while True:
        start_input = input('Type \'1\' and press enter to start a new story at Oxbridge University\nor type \'2\' to continue your previous story.\n>>> ')
        if start_input == '1':
          while True:
            confirm = input('Please confirm that you want to START OVER\n(y/n)>>> ')
            if confirm in y_n_resp:
              if confirm == 'y':
                os.remove('save_file.json')
                confirmed = True
                create_player(player)
                break
              elif confirm == 'n':
                break
              print('That\'s an invalid input, please try again.')
          break
        elif start_input == '2':
          while True:
            confirm = input('Please confirm that you want to LOAD SAVE\n(y/n)>>> ')
            if confirm in y_n_resp:
              if confirm == 'y':
                confirmed = True
                load_save(player)
                break
              elif confirm == 'n':
                break
            print('That\'s an invalid input, please try again.')
          break
        print('That\'s an invalid input, please try again.')
  else:
    player = Player('')
    print(
      start_screen_title,
      start_new,
      intro
    )
    start_input = None
    while True:
      start_input = input('Type \'1\' and press enter to start your life at Oxbridge University!\n>>> ')
      if start_input == '1':
        create_player(player)
        break
      print('That\'s an invalid input, please try again.')

if __name__ == "__main__":
  launch()