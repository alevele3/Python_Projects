# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. 
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

# number of cans = (wall height ✖️ wall width) ÷ coverage per can.

# e.g. Height = 2, Width = 4, Coverage = 5

# number of cans = (2 ✖️ 4) ÷ 5

# = 1.6

import math
import os

hei = int(input("Height: "))
wid = int(input('Widht: '))
cov = int(input('Coverage area: '))

def cans(height, width, coverage):
    height = float((input('What is the height ')))
    width = float((input('What is the width: ')))
    coverage = (5)

    latas = (math.ceil(width * height / coverage))
    latas_b = ((width * height / coverage)) # ROONDING UP THE RESULT.


    print(f'The number of cans of paint is:  \n {latas}')
    print(f'The number of cans, NOT ROUNDED UP: \n  {latas_b}')


h = 0
w = 0
c = 5

def can_2(height, width, coverage):
    can = height*width/coverage
    print(f'Can_2 function keyword_Args: \n {can}')

os.system('clear') # CLEARS THE SCREEN

cans(h, w, c)
can_2(height=hei, width=wid, coverage=cov) # KEYWORD ARGUMENTS
