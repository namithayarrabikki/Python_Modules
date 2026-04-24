import random

secret_number=random.randint(1,100)
while True:
        guess=int(input("guess a number between 1 and 100:"))
        if guess > secret_number:
                print("too high! try agian.")
        elif guess < secret_number:
            print("too low! try agian.")
        else:
            print(f" congratulations! you guessed the correct number:{secret_number}")
            break
