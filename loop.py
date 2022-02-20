#1
for i in range (45,210) :
    if i ==100:
        continue
            
    elif i == 205 :
     break
    print (i)
#2
# xx=input(" what is the product of 7 * 24 ?")
# if xx ==186:
#  while xx ==168:
#     print("You answered this Question correctly")
#     break
# else:
#     print(" Your Answer is wrong try again..")
# xx=input(" what is the product of 7 * 24 ?")
# anser= str (168)
# while xx ==186 :
#     print("You answered this Question correctly")

xx= 7 * 24

while True:
    answer = input("what is the product of 7 * 24 ?")
    if int(answer) == xx:
        print ("You answered this Question correctly")
        break
    else:
        print("Your Answer is wrong try again:")
    
