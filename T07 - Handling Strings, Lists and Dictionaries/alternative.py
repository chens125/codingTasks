
######## First Programme #########################
#This program can read a string and makes each alternate character into an upper case character
#and each other alternative character a lower case character
string="Hello World"
string_list=list(string)

# wrong solution:string[3]=string[3].lower()
#Strings in Python are immutable, which means you cannot directly modify individual characters in a string using indexing and assignment like string[3] = some_value. This operation will raise a TypeError.


for i in range(len(string_list)):
    if i%2==0:
        string_list[i]=string_list[i].upper()
    else:
        string_list[i]=string_list[i].lower()
new_string=''.join(string_list)
print(new_string)

######## Second Programme ######################### 
#making alternative word lower and upper case
string1="I am learing to code"
string_split=string1.split()

for i in range(len(string_split)):
    if i%2==0:
        string_split[i]=string_split[i].lower()
    else:
        string_split[i]=string_split[i].upper()
new_string1=' '.join(string_split)
print("\n",new_string1)