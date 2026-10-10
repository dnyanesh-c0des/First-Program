import random

player_score=0
computer_score=0

print("==================================")
print("Welcome to Rock Paper Scissors!")
print("==================================")

while True:
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        player_choice = input("Enter your choice (1-4): ")

        if player_choice == '4':
            print(f"\nFinal Scores:")
            print(f"You: {player_score}")
            print(f"Computer: {computer_score}")
            print("Thanks for playing!")
            break

        if player_choice not in ['1', '2', '3']:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(['1', '2', '3'])

        choices = {'1': 'Rock', '2': 'Paper', '3': 'Scissors'}

        print(f"\nYou chose: {choices[player_choice]}")
        print(f"Computer chose: {choices[computer_choice]}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == '1' and computer_choice == '3') or \
             (player_choice == '2' and computer_choice == '1') or \
             (player_choice == '3' and computer_choice == '2'):
              print("You win!")
              player_score = player_score + 1
        else:
              print("Computer wins!")
              computer_score = computer_score + 1

        print(f"\nFinal Scores:")
        print(f"You: {player_score}")
        print(f"Computer: {computer_score}")