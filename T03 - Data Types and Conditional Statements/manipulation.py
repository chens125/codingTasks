#This Python file is for 10-003-01 Auto-graded Task 1 

str_manip=input("Please enter a sentence.")

print("The length of the sentence is " + str(len(str_manip))+ ".")

#Replacing Task
import re
last_letter=str_manip[-1]
new_str_manip=re.sub(last_letter,"@",str_manip)
print(new_str_manip)

#last three characters backwards
print(str_manip[-1:-4:-1])

#creating 5-letter word
print(str_manip[:3]+str_manip[-2:])