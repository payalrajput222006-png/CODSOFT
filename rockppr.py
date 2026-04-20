import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
rounds = 5

print("🎮 Welcome to Rock Paper Scissors (Best of 5)")

for round_no in range(1, rounds + 1):
    print(f"\n--- Round {round_no} ---")

    user = input("Enter rock/paper/scissors: ").lower()

    # Input validation
    if user not in choices:
        print("Invalid input! Try again.")
        continue

    computer = random.choice(choices)

    print("You:", user)
    print("Computer:", computer)

    if user == computer:
        print("It's a tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win this round!")
        user_score += 1

    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score ➤ You: {user_score} | Computer: {computer_score}")

# Final Result
print("\n Final Result:")
print(f"You: {user_score} | Computer: {computer_score}")

if user_score > computer_score:
    print("🎉 Congratulations! You won the game!")
elif user_score < computer_score:
    print("You lost the game!")
else:
    print("It's a draw!")

# Replay option
while True:
    replay = input("\nDo you want to play again? (yes/no): ").lower()
    if replay == "yes":
        print("Restart the program to play again!")
        break
    elif replay == "no":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input!")