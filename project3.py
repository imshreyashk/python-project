import random

name = input("What is your name? ")
print("Good Luck !", name)

words = ['rainbow', 'computer', 'science', 
         'programming', 'python', 'mathematics', 'player',
         'condtion', 'reverse', 'water', 'board']

word = random.choice(words)

print("Guess the character! ")

guesses = ''

turn = 11

while turn > 0:

    #count the number of times a user fails
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print(" ")

            failed += 1
    
    if failed == 0:
        print("You win")

        print("The word is:", word)

    #if user has input the wrong alphabet then
    #it will ask user to enter another alphabet
    print()
    guess = input("Guess a character: ")

    guesses += guess
    if guess not in word:
        turn -=1

        print("Wrong")

        print("You have", + turn, "more guesses")

        if turn == 0:
            print("You loose")