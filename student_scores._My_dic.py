import os


my_dic = {
  "Carro": "volvo", "Pc": "dell", "Shoe": "adidas"
}

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
my_emp = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
#os.system('clear')
os.system('clear')
print(f'Student Scores = \n {student_scores} \n ')
print(f' My Dic = {my_dic} \n ')
for student in student_scores:    # 'student' is the 'key', 
    score = student_scores[student] # Here we access the 'value' of the Key 'Student'.
    if score > 90:
      student_grades[student] = 'Outstanding'
    elif score > 80:
      student_grades[student] = 'Exceeds Expectations'
    elif score > 70:
      student_grades[student] = 'Accepatable'
    else:
      student_grades[student] = 'Fail'

    #print(student)
    #print(student_scores)
    #print(student_scores[student])

#print(student_scores) 
val = input('Enter value expecte: \n')
for key in my_dic:
  value = my_dic[key]
  if val == key:
    print(f"is a key: {key} and its value is = {value} \n ")
    my_emp[key] = 1
  elif val == value:
    #print(f' Is Vslue: {value} \n ')
    print(f'Is value: {value}, with Key: {key} \n ')
print(my_emp)
  # elif val == 
  #   print('Is a Dell')
  # else:
  #   print('Nor a Carr or a Dell')

# 🚨 Don't change the code below 👇

print(student_grades)

