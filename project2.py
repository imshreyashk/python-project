import random
import math

 #taking inputs
lower = int(input("Enter lower bound: "))

upper = int(input("Enter upper bound: "))


#generating random number between the lower and upper

x = random.randint(lower, upper)
total_chance = math.ceil(math.log(upper - lower +1, 2))
print("\n\tYou've only", total_chance, "chances to guess the integer!\n")



# Initializing the number of guesses.
count = 0
flag = False

#for calculation of minimum number of guesses depends upon range
while count < total_chance:
    count += 1

    guess = int(input("Guess a number: "))
    if x == guess:
        print("Cingratulations you didi it in ", count, " try")

        flag = True
        break
    elif x > guess:
        print("You guessed too hight")
    else:
        print("You guessed too high! ")

if not flag:
    print("\n The number is %d" % x)
    print("\t Btter Luck Next time!")
