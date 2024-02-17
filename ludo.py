import random

# Initialize the Ludo board
board = [[0] * 15 for _ in range(15)]

# Initialize players and their tokens
players = ['Player 1', 'Player 2', 'Player 3', 'Player 4']
tokens = {'Player 1': ['P1A', 'P1B', 'P1C', 'P1D'],
          'Player 2': ['P2A', 'P2B', 'P2C', 'P2D'],
          'Player 3': ['P3A', 'P3B', 'P3C', 'P3D'],
          'Player 4': ['P4A', 'P4B', 'P4C', 'P4D']}

# Initialize token positions
token_positions = {player: {} for player in players}

# Function to roll a dice
def roll_dice():
    return random.randint(1, 6)

# Function to display the board
def display_board():
    for row in board:
        print(' '.join(map(str, row)))
    print()

# Function to move a token
def move_token(player, token, steps):
    current_position = token_positions[player].get(token, (0, 0))
    x, y = current_position
    new_x = x + steps
    if new_x >= 15:
        new_x = 14
    if new_x < 0:
        new_x = 0
    token_positions[player][token] = (new_x, y)

# Function to play a turn
def play_turn(player):
    input(f"{player}'s turn. Press Enter to roll the dice...")
    steps = roll_dice()
    print(f"{player} rolled a {steps}.")
    token = input(f"Choose a token to move ({', '.join(tokens[player])}): ")
    
    if token not in tokens[player]:
        print("Invalid token.")
        return

    move_token(player, token, steps)
    display_board()

# Main game loop
while True:
    for player in players:
        display_board()
        play_turn(player)

        # Check for a win condition
        if all(position[0] >= 14 for position in token_positions[player].values()):
            print(f"{player} wins!")
            exit()
