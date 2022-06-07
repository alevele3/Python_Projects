
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

#TODO-2: Write your code below to add the grades to student_grades.👇
#os.system('clear')
for student in student_scores:# 'student' is the 'key', 
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

# 🚨 Don't change the code below 👇
print(student_grades)

