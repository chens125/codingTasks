lolstring = "  Hello,  World!  "


print(lolstring.lower())
print(lolstring.upper())
print(lolstring.strip())
print(lolstring.strip(","))

print(lolstring.find("!"))

print(lolstring.replace("o", "@"))

print(lolstring.split("l"))  ##  default is white space
print(lolstring.split())

# lolstring.append()

# "".join(string_list)

print('Hello \n"bob"')


#########    String building   ####################
number_builder = ""
i = 0

while i < 50:
    if i % 2 == 0:  # 可以整除2； even
        number_builder += str(i) + " "
    i += 1
print(number_builder)

while i < 50:
    if i % 2 == 0:
        number_builder.append(str(i))
    i += 1
print("".join(number_builder))


# =========== Python list Methods  ===========
# There are many useful built-in list methods available for you to use.
# Some other list methods can be found below:
#   extend()    - Adds all elements of a list to the another list
#   insert()    - Inserts an item at the defined index
#   remove()    - Removes an item from the list
#   pop()       - Removes and returns an element at the given index
#   index()     - Returns the index of the first matched item
#   count()     - Returns the count of number of items passed as an argument
#   sort()      - Sorts items in a list in ascending order
#   reverse()   - Reverses the order of items in the list

######### nested lists#######
a = [1, 2, 3]
b = [4, 9, 8]
c = [a, b, "tea,16"]
print(c)
c.remove(b)
print(c)

######### Copying lists ######################
a = [1, 2, 3]
b = a[:]  # creat a copy
b[1] = 10
print(a)
print(b)

a = [4, 5, 6]
b = a
a[0] = 10
print(b)  # shallow copy

import copy

a = [[1, 2, 3], [4, 5, 6]]
b = a[:]
c = copy.deepcopy(a)

b[0][1] = 10
c[1][1] = 12
print(a)
print(b)
print(c)


# ============= Deleting Elements From a list ==================
# You can use the 'del' keyword to delete one or more items from a list.
# You are even able to delete the list entirely.

# ************ Example 8 ************
print("\nExample 8:")

char_list = ["P", "y", "t", "h", "o", "n"]

del char_list[3]
# Deletes the single element 'h'
print(char_list)

del char_list[1:3]
# Deletes multiple elements from the 2nd to 4th element.
print(char_list)

del char_list
# Deletes the entire list


# ================== Checking if Something is in a List ==================
# You can simply use an if statement to check if a certain item is in a list.

# ************ Example 12 ************
print("\nExample 12:")
grocery_list = ["Bread", "Milk", "Butter", "Cheese", "Cereal"]

if "Apples" in grocery_list:
    print("The item Apples was found in the list grocery_list")
else:
    print("The item Apples was not found in the list grocery_list")

# This is a much quicker way than looping through all the items, such as if you did:
for item in grocery_list:
    if item == "Apples":
        print("The item Apples was found in the list grocery_list")

######### List comprehension###########
num_list = ["1", "5", "8", "14", "25", "31"]
new_num_list_ints = [int(element) for element in num_list]
print(new_num_list_ints)


########## Dictionaries ###############
# lists are ordered sets of elements, whereas dictionaries are unordered sets
# list: access via index position
# Dictionaries: access via keys
int_key_dict = {1: "apple", 2: "banana", 3: "arange"}
keys = int_key_dict.keys()
values = int_key_dict.values()
print("hey here")
print(keys)
print(values)

# or creat from a list with dict() function:
int_key_list = [(1, "apple"), (2, "banana")]  # tuple
int_key_dict = dict(int_key_list)

# pattern matching
my_tuple = (1, "apple")
key, value = my_tuple
print(key)
print(value)

##changing elements ina dictionary
int_key_dict = {1: "apple", 2: "banana", 3: "arange"}
int_key_dict[1] = "kiwi"
print(int_key_dict)

int_key_dict[5] = "apple"
print(int_key_dict)

####membership test
print(2 in int_key_dict)
