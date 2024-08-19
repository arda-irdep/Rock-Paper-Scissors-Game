import random

print("Welcome to Rock, Paper, Scissors!")

while True:
    counter = 0
    user_score = 0
    computer_score = 0
    answer = "yes"

    while counter != 3 and answer == "yes":
        user_choice = input("Type 'rock', 'paper', or 'scissors' to choose your move or 'exit' to quit the game:\n\n")
        print("\nUser chose: " + str(user_choice))

        if user_choice == "exit":
            print("Goodbye...")
            break

        comp_choice = random.choice(["rock", "paper", "scissors"])
        print("\nComputer chose: " + str(comp_choice))

        if (user_choice == 'rock' and comp_choice == 'scissors') or \
           (user_choice == 'scissors' and comp_choice == 'paper') or \
           (user_choice == 'paper' and comp_choice == 'rock'):
            print("\nUser wins\n")
            user_score += 1

        elif user_choice == comp_choice:
            print("\nTie\n")

        else:
            print("\nComputer wins\n")
            computer_score += 1

        counter += 1

        if user_score == 2:
            print("\nUser wins the game!\n")
            break

        elif computer_score == 2:
            print("\nComputer wins the game!\n")
            break

    print("User Score: " + str(user_score) + "\nComputer Score: " + str(computer_score))
    
    answer = input("Do you want to play again? (yes/no): ").lower()
    if answer == "yes":
        comp_decision = random.choice(["yes", "no"])
        if comp_decision == "no":
            print("Computer has decided not to play again. Thanks for playing! Goodbye!")
            break
    else:
        print("Thanks for playing! Goodbye!")
        break
