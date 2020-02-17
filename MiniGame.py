import random
secretNumber = random.randint(0, 10)
count = 0
userInput = ""
while userInput != secretNumber:
    userInput = int(input("Can you guess, what the number is it? "))
    if userInput == secretNumber:
        print("Yeaaaaahhh, you find it!!!!!! ", "The secret number is ", secretNumber)
        break
    elif userInput > secretNumber:
        count += 1
        print("Lower , lower )))")
    elif userInput < secretNumber:
        count += 1
        print("Bigger , bigger ...")

