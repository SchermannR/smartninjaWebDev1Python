
choice = 5

for x in range(1,choice+1):
    print(x)

for y in range(1,choice):
    print(y)

for z in range(choice):
    print(z)

a=["a","b","c","d","e","f","g"]


print(type(len(a)))
print(type("\r\n\r\n"))
#print("\r\n\r\n"+str(len(a))) #\r\n for windows \n only for linux
print("\r\n\r\n")
print(len(a))


for v in range(len(a)):
    #a[0] first attempt - a
    #a[1] second attempt - b
    #a[2] third attempt -c
    print(a[v])
    if a[v] == "d":
        break;
a[v] = "l"

print(a[0])
print(a[1])
print[a[2]]
print[a[3]]
print[a[4]]
print[a[5]]
print[a[6]]

#hello
"""
asdafdsafsdfsafs
asdasdffdsf
"""


import random

secret = random.randint(1, 30)
attempts = 0
print(secret)

with open("score.txt", "r") as score_file:
    best_score = int(score_file.read())
    print("Top score (attempts): " + str(best_score))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1 #attempts=attempts+1; e.g. in C: attempts++

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        if attempts < best_score:
            with open("score.txt", "w") as score_file:
                score_file.write(str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")



