#strings
name="siyu"
long_string='''this is a long string
using triple quotes preserves everything inside it as a string
even on a different lines and with different spacing'''

#string concatenation
name="john"
surname="peter"
full=name+surname
full1=name+" "+surname

#note that concatenate a string and a non-string
#but
print(full1+str(32))

#or format() method,在句尾
age=32
country="UK"
sentence="My name is {} and I'm {} years old, from {}".format(full1,age,country)
print(sentence)

#F-string#在句首
sentence_2=f"My name is {full1} and I'm {age} years old"
print(sentence_2)

#other functions
#length
greeting="Hello"
print(len(greeting))

#slicing........................................................
print(greeting[1:4])
#return ell

print(greeting[1:])
#return ello

print(greeting[-1])
#return o

print(greeting[0])
#return h

print(greeting[:1])
#return h

print(greeting[1::2])
#return el 
#[begin:end:step]

print(greeting[1::3])
#return eo

print(greeting[4:1:-1])
#return oll

print(greeting[4:1:-2])
#return ol

print(greeting[::-1])
#return olleh

#....................................
new_string="hello good fucking morning"
fizz=new_string[0:5]
print(fizz)
print (new_string)

#.........................
#intergers.....25
#floats.....12.23
#complex....: 45.j
num1=22
num2=99.99
print(float(num1))
print(int(num2)) #return 99
#converting floats to ints casus data loss

########################common function#########################################
number3=66.524876
print(round(number3,2))

numbers_list=[6,4,7,3.9]
print(min(numbers_list))
print(max(numbers_list))
print(sum(numbers_list))

#math module
import math
math.floor(2.34) #2.34 to 2
math.ceil(2.34)  #2.34 to 3
math.trunc(3.14)  #2.34 to 2, cut 小数点
math.sqrt(8) # 4 to 2 
math.pi #3.14.....

#if condition, >,<,==,!,<=,>=,!=

#booleans
#A boolean data type can only store one of two values, nammely True or False. 
#One byte is reserved for storing this data tpye
#Control statement allows you to use booleans to their full potiential
umbrelaa="leave me at home"
rain=False
if rain: ##stand for rain==true
    umbrella="bring me with"


#if-elif-else statements:  can only have many elseif
    
#logical operators: and , or , not

team1_score=3
team2_score=2
game="over"
if (team1_score>team2_score) and (game=="over"):
    print("congrats team1")

speed=int(input("how many km per hour are you travelling at?"))
belt=input("Are you wearing a safty belt?")
if (speed>80) or (belt!="Yes"):
    print("sorry sir, but I have to give a traffic fine")
else:
    print("you can go")
    

    










