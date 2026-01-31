import random       # To generate random values

while True:                 # creating a continuous loop
    # Define Game
    print("\n")
    print("Rock, Paper, Scissors - Shoot!")

    # Taking input from user and normalizing it
    userChoice = input("Choose your weapon [R]ock, [P]aper, [S]cissors, [E]xit: ")

    # Validating the user input
    if userChoice not in ('R', 'P', 'S', 'E'):
        print("Please choose a letter:")
        print("[R]ock, [S]cissors, [P]aper or [E]xit")
        continue

    # Print the user's choice
    print("You chose: " + userChoice)

    # Check if user wants to exit
    if userChoice == 'E':
        print('Exiting Game..')
        break

    # Create a list of possible choices
    choices = ['P','R', 'S']

    # Generating Computer's Choice
    opponentChoice = random.choice(choices)

    # Print Computer's Choice
    print("I chose: " + opponentChoice)

    # Check Computer's Choice and user's Choice by applying game logic
    if opponentChoice == userChoice:         # If both chose same value, it's a tie
        print("Tie!")
    elif opponentChoice == 'R' and userChoice == 'S':            # Rock Vs Scissors - Rock/computer Wins
        print("Rock beats Scissors, I win!")
    elif opponentChoice == 'S' and userChoice == 'P':            # Scissors Vs Paper - Scissors/computer Wins
        print("Scissors beats Paper, I win!")
    elif opponentChoice == 'P' and userChoice == 'R':            # Paper Vs Rock - Paper/computer Wins
        print("Paper beats Rock, I win!")
    else:                                                                 # In all the other cases, user wins!
        print("You win!")