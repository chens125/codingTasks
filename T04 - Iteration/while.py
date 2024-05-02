# while loop

number = int(input("Dear user, please enter a number:"))

count = 0
sum = 0
while number != -1:
    count += 1
    sum = sum + number
    number = int(input("Dear user, please enter a number:"))
    if number == -1:
        break
print(sum, count)
print(sum / count)
