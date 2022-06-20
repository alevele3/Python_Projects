import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# paswrd = ""
# for char in range(1, nr_letters + 1):
#   paswrd += random.choice(letters)
#   #print(paswrd)  

# for cher in range(1, nr_numbers + 1):
#   paswrd += random.choice(numbers)
#   #print(paswrd)  

# for chir in range(1, nr_symbols + 1):
#   paswrd += random.choice(symbols)
  
# print(paswrd)  





#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

paswrd = []
for char in range(1, nr_letters + 1):# 'FOR LOOP' to scan all letters at the range given by the user with 'range(1, nr_letters + 1)'
  paswrd += random.choice(letters)# all these 'LETTERS' in the list
  # of 'letters' and as this is done, in line 38, we 'COLLECT'
  # ALL THESE letters by adding them to 'paswrd' and random
  # ize them with 'random.choice(letters)'

for cher in range(1, nr_numbers + 1):
  paswrd += random.choice(numbers)
  #print(paswrd)  

for chir in range(1, nr_symbols + 1):
  paswrd += random.choice(symbols)

print(paswrd)
random.shuffle(paswrd)# Here we randomize the order of all the elements types in the list 'paswrd' making it harder to crack. The function 'shuffle' is employ in line 51 to acomplish this.
print(paswrd)

pas = "" # We crate a variable type string, to convert all the elements in 'paswrd' to string characters, by using the 'for loop'
for i in paswrd:
  pas += i
# Here with every iteration of the loop, each element of 'paswrd' is placed in the variable 'i' and concurrently, this variable latest content gest added to 'pas', where all the elements are agregated together forming one single string.

print(pas)