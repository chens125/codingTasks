###To design a program that determines the award a person competing in a triarhlon will receive
print("Please input the information below to check award eligibility")
name = str(input("Please enter the participant's name:"))
swim = input("Time for swimming (in minutes):")
cycle = input("Time for cycling (in minutes):")
run = input("Time for running (in minutes):")

total_time = round((float(swim) + float(cycle) + float(run)), 2)
print(
    "Total time taken for "
    + name
    + " to complete the triathlon is "
    + str(total_time)
    + " minutes"
)

if total_time < 101:
    print("Congrats" + name + ", you won a Provincial Colours Awards")
elif total_time < 106:
    print("Congrats" + name + ", you won a Provincial Half Colours Awards")
elif total_time < 111:
    print("Congrats" + name + ", you won a Provincial Half Colours Awards")
else:
    print("Sorry" + name + ", you have no awards this time")
