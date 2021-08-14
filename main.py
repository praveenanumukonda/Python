
hungry = input("Are you hungry: ")

if hungry == 'yes':
    print("Eat Biryani")
else:
    print('Do work')

i = 0

fruits = ["apple", "banana", "cherry"]
fruit = input("Enter your fav fruit: ")
for x in fruits:
    print(x)
    if x != fruit:
        continue
    break
