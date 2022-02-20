
from tkinter.messagebox import QUESTION


for number in range(45, 210):
    if number == 100:
        continue
    elif number == 205:
        break
    print(number)


quiston = input("what is the product of 7 * 24 ?")
print(quiston)

converToint = int(quiston)
while converToint == 168: 
    # converToint=+1
    print("You answered this Question correctly")
    break
else :
    print("Your Answer is wrong try again..")
quiston = input("what is the product of 7 * 24 ?")
