# 1)
numbers = range(45, 210)
for num in numbers:
    if num == 100:
        continue
    elif num == 206:
        break
    print(num)


# 2)
state = True
while state:
    result = input("what is the product of 7 * 24?")
    if int(result) == 168:
        print("You answered this Question correctly")
        state = False
    else:
        print("Your Answer is wrong try again..")
        state = True
