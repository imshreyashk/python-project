# python-project
import random

# Define symbols and their payouts
symbols = ["cherry", "orange", "plum", "bell", "7"]
payouts = {
    "cherry": 1,
    "orange": 2,
    "plum": 3,
    "bell": 5,
    "7": 10,
}

# Function to spin the reels
def spin_reels():
  reel1 = random.choice(symbols)
  reel2 = random.choice(symbols)
  reel3 = random.choice(symbols)
  return [reel1, reel2, reel3]

# Function to check for winning combinations
def check_winnings(reels, bet):
  # Check for all three symbols matching
  if reels[0] == reels[1] == reels[2]:
    return payouts[reels[0]] * bet
  # No win
  return 0

# Start the game
balance = 100  # Starting balance
while True:
  # Print current balance
  print(f"Balance: ${balance}")

  # Get player's bet
  while True:
    try:
      bet = int(input("Enter your bet ($1 minimum): "))
      if bet >= 1 and bet <= balance:
        break
      else:
        print("Invalid bet amount. Please enter a number between 1 and your current balance.")
    except ValueError:
      print("Invalid input. Please enter a number.")

  # Spin the reels
  reels = spin_reels()
  print(f"Reels: {reels[0]} {reels[1]} {reels[2]}")

  # Calculate winnings
  winnings = check_winnings(reels, bet)

  # Update balance
  balance += winnings - bet

  # Print outcome
  if winnings > 0:
    print(f"You won ${winnings}!")
  elif winnings == 0:
    print(f"No win. Try again!")
  else:
    print(f"You lost ${bet}.")

  # Ask to play again
  play_again = input("Play again? (y/n): ")
  if play_again.lower() != "y":
    break

# End game message
print(f"Thanks for playing! You finished with ${balance}.")
