# Solution
print("my solution")
stars = "*****"
index = 1
for index in range(0, 10):
    if index < 6:
        print(stars[0:index])
    else:
        print(stars[0 : (10 - index)])


####I will try other ways####
print("I will try other ways")
print("The first way")
star = "*"
count = 1
for count in range(1, 10):
    if count < 6:
        print(star * count)
        count += 1
    else:
        print(star * (10 - count))
        count += 1

########2nd way:without if_else##########
print("The second way")
star = "*"
count = 1
for count in [1, 2, 3, 4, 5, 4, 3, 2, 1]:
    print(star * count)


########3rd way:while_loop##########
print("The third way")
star = "*"
count = 1
while count <= 9:
    if count < 6:
        print(star * count)
        count += 1
    else:
        print(star * (10 - count))
        count += 1
