
import os

from curses import keyname


programming_dictionary = {

"Bug": "An error in a program that prevents the program from running as expected.", 
"Function": "A piece of code that you can easily call over and over again.", 
123: "123"
}

#print(programming_dictionary[123])

programming_dictionary["loop"] = "The repeating action"

os.system('clear')
print(f'1 Key-Value pairs : \n  {programming_dictionary} \n ')

print(f'2 Key = "Function": {programming_dictionary["Function"]} \n')

empty_dictionary = {}

# wipr an existing dictionary :

#programming_dictionary = {}
#print(str("  Wiped version: " + programming_dictionary))# ERROR
print(f'3 Key-Value pairs : \n {programming_dictionary} \n')
print(f'4 "Empty" {empty_dictionary} \n')
print(f'5 Key = "Loop": {programming_dictionary["loop"]} \n')

for key in programming_dictionary:
    print(f'Key = {key} \n ')
    print(f'Value = {programming_dictionary[key]} \n')