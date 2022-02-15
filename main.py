
# Q1 : 
temp = range(45,211)
for n in temp:
    if n == 100:
        continue
    if n == 205:
        break
    print(n)

# Q2 :
while True:
    result = input('What is the product of 7 * 24 ? ')
    if result == str(7*24) :
        break
    print('Your Answer is wrong try again..')
print('You answered this Question correctly')