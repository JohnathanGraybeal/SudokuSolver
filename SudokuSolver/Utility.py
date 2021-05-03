<<<<<<< HEAD
from os import system, name

#Just a utility function to clear output screen
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
=======
from os import system, name

#Just a utility function to clear output screen
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
>>>>>>> 1bb178033012db5a5d68bb7d51fe163839e13144
