for x in range(45,210):
    if x ==100:
        continue
    elif x==205:
        break
    else:
        print(x)


product=input("what is the product of 7 * 24 ?")
while product != "168" :
    print("Your Answer is wrong try again..")
    product=input("what is the product of 7 * 24 ?")
else:
    print( "You answered this Question correctly")  
