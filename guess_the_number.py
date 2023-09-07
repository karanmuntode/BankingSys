import random

number = random.randint(1, 100)

attempts = 1

while(attempts <= 10):
    print(f"\nAttempt {attempts}")
    user_guessed = int(input("Guess the number between (1 - 100) : "))
    if(user_guessed > number):
        print("Try a lower number please!")

    elif (user_guessed < number):
        print("Try a higher number please!")

    else:
        print("You Won!")
        print("Your guess is correct!")
        break

    attempts += 1

print(f"The number was : {number}")

if(attempts > 10):
    print("GAME OVER!")

