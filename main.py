# College life sim
import json
import os
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
    pass

player = Student()

def load_save():
  with open('save_file', 'r') as save:
    data = save.read()
    save_data = data
  print(save_data)

def start():
  player_name = input('What\'s your name?\n')
  print ('Hello', player_name)
  player.name = player_name

  save_data = {
    'player_name': player.name,
    'current_season': School.season,
    'current_day': School.day
  }

  with open('save_file', 'w') as save:
    json.dump(save_data, save)

def launch():
  if os.path.exists('save_file') == True:
    print(
      start_screen_title,
      start_new_or_load
    )
    start_input = None
    while True:
      start_input = input('Type \'1\' and press enter to start a new story at Oxbridge University\n or type \'2\' to continue your previous story.')
      if start_input == '1':
        start()
        break
      elif start_input == '2':
        load_save()
        break
      print('That\'s an invalid input, please try again.')
  else:
    print(
      start_screen_title,
      start_new,
      intro
    )
    start_input = None
    while True:
      start_input = input('Type \'1\' and press enter to start your life at Oxbridge University!\n')
      if start_input == '1':
        start()
        break
      print('That\'s an invalid input, please try again.')

launch()