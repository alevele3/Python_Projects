import os

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(nation, vis, cities): # Parameters =  'VALUE'
   new_pais = {}
   new_pais['paiz'] = nation  # Key = 'paiz', value = function argument 'nation'
   new_pais["paradas"] = vis    # Key = 'paradas', value = function argument 'vis'
   new_pais["lugares"] = cities # Key = 'lugares', value = function argument 'cities'
   travel_log.append(new_pais)  # Add the new list item (Dictionaty = 'new_pais')
                                # to the list 'travel_log'    
   print(f'Nuevo pais: {new_pais} \n')

os.system('clear')


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



