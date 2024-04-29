# This program will read DOB.txt and print out information in different format

#Step 1: Initialize variables for name and date of birth (dob)
name="\nName\n"
dob="\nBirthdate\n"

#Step 2: Open the file
#Step 3: Loop through each line in the file
with open('DOB.txt','r') as info_file:
    for line in info_file:

        ## Step 4: Extract the first two words as the name, append new_name to the name variable
        new_name=" ".join(line.split()[:2])
        name=name+"\n"+new_name
        
        ## Step 5: Extract the last three words as the date of birth, etc
        new_dob=" ".join(line.split()[-3:])
        dob=dob+"\n"+new_dob

## Step 6: Print the formatted name and date of birth
print(name)
print("\n"+dob)




