import random

# Options for the game
choices = ["rock", "paper", "scissors"]

while True:
    # User input
    user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
    
    if user_choice == "exit":
        print("Thanks for playing!")
        break

    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue

    # Computer choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

    print()  # Add a blank line for readability
