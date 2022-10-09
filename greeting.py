# Add a feature to your application that will accept an input that asks the user to pick from at least 3 different greetings. Obviously the default option should be "Southern"


from contextlib import nullcontext


def say_hello():

    greeting_1 = "Hey girl hey!"
    greeting_2 = "Whats happening?"
    greeting_3 = "Hello there!"
    greeting_default = "Hey y'all!"
    greeting = 'Please choose a greeting:' + '\n' + greeting_1 + \
        '\n' + greeting_2 + '\n' + greeting_3 + '\n' ':'

    x1 = input('What is your name?')
    print(x1)

    if input(greeting):
        x2 = input(greeting)
        print(x1 + ',' + x2)
    else: input(greeting) == None
    print(x1 + " " + greeting_default)


say_hello()
