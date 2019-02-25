secret = 22
guess = 0

print(type(secret))

while guess != secret:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You guessed it - congratulations! It's number 22.")
    elif guess > secret:
        print("Sorry, your guess is not correct... The secret number is smaller than " + str(guess))
    else:
        print("Sorry, your guess is not correct... The secret number is smaller than " + str(guess))
"""
    else:
        print("Sorry, your guess is not correct... The secret number is not " + str(guess))
"""

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You guessed it - congratulations! It's number 22.")
        break
    elif guess > secret:
        print("Sorry, your guess is not correct... The secret number is smaller than " + str(guess))
    else:
        print("Sorry, your guess is not correct... The secret number is smaller than " + str(guess))

for x in range(5):
    print("loop repeated" + str(x) + " times of " + str(range(5))+"\n")
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You've guessed it - congratulations! It's number 22.")
        break
    else:
        print("Sorry, your guess is not correct... The secret number is not " + str(guess))

for a in range(5):
    print("Outerloop a= " + str(a))
    for b in range(5):
        print("\tInnerloop b= " + str(b))
"""
for y in range(5):
    print("Outerloop y= "+str(y))
    for c in range(5):
        guess = int(input("Guess the secret number (between 1 and 30): "))
        print("inner loop c= " + str(c))
        if guess == secret:
            print("You've guessed it - congratulations! It's number 22.")
            break
        else:
            print("Sorry, your guess is not correct... The secret number is not " + str(guess))
"""