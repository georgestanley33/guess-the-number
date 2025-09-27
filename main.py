import random

number = random.randint(1,100)
print(number) #For testing

while True:
    choice = int(input("Guess a number between 0 and 100"))
    if choice == number:
        print("Well done, you guessed the number!")
        break
