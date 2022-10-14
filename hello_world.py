# print("Howdy Y'all!!");

# animals = [ "Triceratops", "Gorilla", "Corgi", "Toucan"]

# for animal in animals:
#     print(animal)

from pickle import NONE
import random 



def length_of_string() :
  
    animals = [ "Triceratops", "Gorilla", "Corgi", "Toucan", "Cat"]
    for animal in animals :
      if len(animal) >= 5:
        print(animal)
# length_of_string()

def funny_animal_names_prompt() :
  
  
    prompt_animal_names = input("Create some funny animal names:").split(',')
    
    print("Hi there! These are the names you've submitted:")
  
    for animals in (prompt_animal_names):
      print(animals)
    
   
# funny_animal_names_prompt()


def fav_animal():
  
  animals = [ "Triceratops", "Gorilla", "Corgi", "Toucan", "Cat"]

  fave = input('What is your favorite color?' + '\n')
  
  print(f'I would like to have a {fave} {random.choice(animals)}')

fav_animal()



   
  #    prompt_animal_names = input("Create some funny animal names:")
   
  #  animal_names = []
   
  #  animal_names.append(prompt_animal_names)
   
  #  for animal_name in animal_names:
   
  #   print("Hi there! These are the names you've submitted:")
    
  #   for animal_name in (animal_name, 1):
   
  #     print(animal_names)
   
 # while input(response):
  #  prompt_animal_names = input("Create some funny animal names:")
   
  #  animal_names = []
   
  #  animal_names.append(prompt_animal_names)
   
   
  #  for count, name in enumerate(animal_names, 1):
   
  #   print("Hi there! These are the names you've submitted:")
  #   print(count, name) 


#   i = input()
  
#   while i :
  
#     print(prompt_animal_names)
#     break
#   else:
#     for count, name in enumerate(prompt_animal_names, 1):
   
#       print("Hi there! These are the names you've submitted:")
#     print(count, name + '\n') 

  
   
# funny_animal_names_prompt()
