import random
import time


attempts = 0
pin = random.randint(1111,9999)
guess = random.randint(1111,9999)
correct = False

while correct == False:
    time.sleep(0.01)
    print(guess)
    if guess == pin:
        correct = True
        print("You guessed correctly in", attempts, "attempts")
    else:
        guess = random.randint(1111,9999)
        attempts = attempts +1 