# This program allows a user to register students for an exam venue

# Step 1: Prompt the user to input the number of students registering
# Step 2: Open the file 'reg_form.txt' in write mode (w+)
# Step 3: Write the header for the attendance register
# Step 4: Loop through each student
# Step 5: Prompt the user for each student's ID number
# Step 6: Write the student's ID to the file

#Checking:
# Step 7: Open the file 'reg_form.txt' in read mode
# Step 8: Print the contents of the file

#Step 1
num_student=int(input("How many student are registering?   "))

#Step 2
with open("reg_form.txt", 'w+') as id_info:
    id_info.write("EXAM ATTENDENCE REGISTER")  #Step 3
    for i in range(1,num_student+1):           #Step 4
        print(f"\nThis is student number {i}.")
        student_id = input("Please enter the student's ID number: ") #Step 5
        id_info.write(f"\n{student_id}..............................") #Step 6


# Step 7&8
with open('reg_form.txt','r') as form_check:
    print("\n"+form_check.read())
