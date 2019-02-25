import random


secret = random.randint(1, 30)
print(secret)

while True:

    try:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        if guess == secret:
            print("You've guessed it - congratulations! It's number " + str(secret))
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")
    except:
        print ("Could not convert data to an integer.")



