for number in range(45, 210):
    if number == 100:
        continue
    elif number == 205:
        break
    else:
        print(number)

state = True

while state:
    product = input("what is the product of 7 * 24 ?")
    if(int(product) == 168):
        print("You answered this Question correctly")
        state = False
    else:
        print("Your Answer is wrong try again..")