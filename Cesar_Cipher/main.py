import os
from turtle import position

from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

def cesar(start_txt, shift_am, cipher_dire):
    end_text = ""
    if cipher_dire == 'decode':
        shift_am *= -1
    for char in start_txt:
        if char in alphabet:
            position = alphabet.index(char)
        # if cipher_dire == 'decode':  # WRONG POSITION FOR THE IF STATEMENT, LINE 16
        #     shift_am *= -1
            new_position = position + shift_am
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f'The {cipher_dire}d text is {end_text} ')

should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #shift = shift % 26  # Here we ensure that the shift ammoung can be any number. OR:
    shift = shift % len(alphabet) #'This way does not work'???

    # TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


    # def cesar(start_txt, shift_am, cipher_dire):
    #     end_text = ""
    #     if cipher_dire == 'decode':
    #         shift_am *= -1
    #     for char in start_txt:
    #         if char in alphabet:
    #             position = alphabet.index(char)
    #         # if cipher_dire == 'decode':  # WRONG POSITION FOR THE IF STATEMENT, LINE 16
    #         #     shift_am *= -1
    #             new_position = position + shift_am
    #             end_text += alphabet[new_position]
    #         else:
    #             end_text += char
    #     print(f'The {cipher_dire}d text is {end_text} ')


    # def encrypt(p_text, am_shft):
    #     cypher_text = " "  # Text varable whre the new letter will be stored in line 22
    #     for l in p_text:

    #         position = alphabet.index(l) # https://www.w3schools.com/python/ref_list_index.asp
    #                                      # WE Acquire the position_index of the letter entered by the user
    #                                      # and save it into 'position'.
    #         new_pos = position + am_shft # Here we add the shift ammount and save the new index into
    #                                      # 'new_pos'.

    #         if new_pos > len(alphabet)-1:       # Here we address the moment where the shift ammount
    #                                             # is greater then the ammount of letters of the
    #             new_pos = new_pos-len(alphabet) # alphabet at the end of the list.


    #         new_l = alphabet[new_pos]    # Here we locate the new letter in the list, by way of new index
    #         cypher_text += new_l         # Here we are saving one after the other all the new letters
    #                                      # into the paramenter variable name 'cypeher_text'.
    #         #cypher_text += alphabet[new_pos]

    #     print(f'Encrypted text is:  {cypher_text}')
    #     print(f'shift: {shift}')

    #     # Now we are going to decrypt

    # def decrypt(cypher_text, a_shft):
    #     norm_text = ''
    #     for l in cypher_text:
    #         pos = alphabet.index(l)
    #         new_pos = pos - a_shft
    #         norm_text += alphabet[new_pos]
    #     print(f'The decoded message is {norm_text}')

        # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text'
        # forwards in the alphabet by the shift amount and print the encrypted text.
        # e.g.
        #plain_text = "hello"
        #shift = 5
        #cipher_text = "mjqqt"
        # print output: "The encoded text is mjqqt"

        # HINT: How do you get the index of an item in a list:
        # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

        # 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    # TODO-3: Call the encrypt function and pass in the user inputs.
    # You should be able to test the code and encrypt a message.
    os.system('clear')
    print(shift)

    cesar(start_txt=text, shift_am=shift, cipher_dire=direction)
    restart = input(f"Type 'y' to go again, or 'n' to stop \n ")
    if restart == 'n':
        should_end = True
        print("Adios...")

    # if direction == 'encode':
    #     encrypt(p_text=text, am_shft=shift) # Keyword arguments
    # elif direction == 'decode':
    #     decrypt(cypher_text=text, a_shft=shift)
