import os

def nomb(name, appe):
    name = input('Enter a name: ') # Entering the POSITIONAL ARGUMENTS 'name'
    appe = input('Enter a last: ') # Entering the POSITIONAL ARGUMENT 'appe'

    print(f'The name is {name} and the last is {appe}')

def nomb2(nam, ap):
    print(f'The name is {nam}, and the last is {ap}')

name = ''
last = ''

os.system('clear') # on linux / os x CLEARS THE SCREEN... FYI

nomb(name, last) # POSITIONAL PARAMETERS name and last. 

nomb2(nam = 'Pacha', ap = 'Diaz')# KEYWORD ARGUMENTS FYI....