# Add a feature to your application that will accept an input that asks the user to pick from at least 3 different greetings. Obviously the default option should be "Southern"


def say_hello():
  
  greeting_1= "Hey girl hey!"
  greeting_2= "Whats happening?"
  greeting_3= "Hello there!"
  greeting_default= "Hey y'all!"
  
  print('Please choose a greeting:' + '\n' +  greeting_1 + '\n' + greeting_2 + '\n' +  greeting_3 + '\n' + greeting_default)
  
  x1 = input()
  print('What is your name?')
  x2= input()
  print(x1 + x2)
  
