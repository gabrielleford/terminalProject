# College life sim
import json

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
  def __init__(self, name):
    self.name = name


player_name = input('What\'s your name?\n')
print ('Hello', player_name)
player = Student(player_name)

save_data = {
  'player_name': player.name
}

with open('save_file', 'w') as save:
  json.dump(save_data, save)


# player_pronouns = ''
# pronoun_choices = {1: 'he/him', 2: 'she/her', 3: 'they/them'}
# player_pronoun_input = input('''
# What are your pronouns?
# 1: he/him
# 2: she/her
# 3: they/them
# ''')
# if player_pronoun_input == 1 or player_pronoun_input == 'he/him':
#   player_pronouns = pronoun_choices[1]
# elif player_pronoun_input == 2 or player_pronoun_input == 'she/her':
#   player_pronouns = pronoun_choices[2]
# elif player_pronoun_input == 3 or player_pronoun_input == 'they/them':
#   player_pronouns = pronoun_choices[3]
# else:
#   print('Sorry, I\'m a very basic terminal game. Those are the only 3 options I have available right now :(')

# print(player_pronouns)