import os

travel_log = {    # Nesting a Dictionary in a Dictionary

    "Colombia": {"cites_visted": {"Bog", "Medallo", "Cali"}, "total_trips": 23},
    "USA": {"citis_been": ["Miami", "New York"]}

}



travel_log2 = [   # Nesting Dictionary in a List.

    # Dictinary 1
    {
    "country": "Colombia",                          # Key value pair 1
    "cites_visted": ["Bog", "Medallo", "Cali"],     # Key value pair 2
     "total_trips": 23                              # Key value pair 3
    },

    # Dictionary 2
    {
    "country": "USA",                       # Key value pair 1
    "citis_been": ["Miami", "New York"],    # Key value pair 2 
    "total_visits": 22                      # Key value pair 3
    },

]
os.system('clear')
print(f'1 Dictionary: \n {travel_log} \n')
print(f'2 List: \n {travel_log2} \n')
