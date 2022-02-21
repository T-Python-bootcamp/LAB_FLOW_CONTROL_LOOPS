# 1
range = range(45, 210)
for loop in range:
    if loop == 100:
        continue
    if loop == 205:
        break
    print(loop)

# 2


answer = 168
while answer == 168:
    uinput = int(input("what is the product of 7 * 24 ? "))
    if uinput == answer:
        print("You answered this Question correctly")
        break
    else:
        print("Your Answer is wrong try again..")
        continue
