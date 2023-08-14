import math
import random

lower = int(input("Enter the lower number: "))
upper = int(input("Enter the upper number: "))

#generating the numbers
x = random.randint(lower, upper)
print("\n\tYou have only ",
      round(math.log(upper - lower + 1, 2)),
      " chances to guess the number!\n")

#initializing the number of guesses
count = 0

#calculating of minimum of guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1

    guess = int(input("Guess a number: "))

    if x == guess:
        print("Congrats You have guessed the right number in ", count, "try.")

        break
    elif x > guess:
        print("That number is too small.")
    elif x < guess:
        print("That number is too high.")
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\t Better luck next time.")
