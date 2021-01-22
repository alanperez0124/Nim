import random

# Opening the names.txt file for the random bots
names = open("names.txt", "r")
first_names = [line.split(" ")[0] for line in names]


class Player:
    def __init__(self, name):
        """Assign the player a name"""
        self.name = name


    def get_move(self):
        """Asks player for input and checks to see if move is valid"""
        valid_move = False
        while not valid_move:
            val = input("Input how many coins you'd like to take away: ")  # place inside to ask again
            try:
                if int(val) not in range(1, 4):
                    raise ValueError
                else:
                    valid_move = True  # will end the while loop

            except ValueError:
                print('Invalid input, please input 1, 2 or 3.')

        return val


class RandomComputerPlayer:
    def __init__(self):
        """Gives the random bot a name from list"""
        self.bot_name = random.choice(first_names)
        print(rf'You will be playing against {self.bot_name}')


    def get_move(self):
        return random.randint(1, 3)


class GeniusComputerPlayer:
    def __init__(self):
        self.bot_name = random.choice(first_names)
        print()
        print(rf'You will be playing against {self.bot_name}')

    def get_move(self):
        return random.randint(1, 3)


class Gameplay:
    def __init__(self):
        self.coins = 12
        self.current_winner = None  # Keeping track of the winner

    def print_coins(self):
        print(" o" * self.coins, '\n')


def play(game, p1, p2, print_game):
    if print_game:
        game.print_coins()

    turn = 'p1'

    while game.coins > 0:
        if turn == 'p1':
            take_away = p1.get_move()

        else:
            take_away = p2.get_move()
            print(rf'{p2.bot_name} took {take_away} coins')

        game.coins -= int(take_away)
        game.print_coins()

        if turn == 'p1':
            turn = 'p2'
        else:
            turn = 'p1'

    if turn == 'p2':
        game.current_winner = p1
        print(f'{p1.name.upper()} WINS!')
    else:
        game.current_winner = p2
        print(f'{p2.bot_name.upper()} WINS!')


# Main body of code
p1 = Player(input('Player 1, please enter your name: '))
choice = input('Would you like to play against a smart AI, a dumb AI, or another human? (1, 2, 3): ')
if choice == '1':
    p2 = GeniusComputerPlayer()
elif choice == '2':
    p2 = RandomComputerPlayer()
elif choice == '3':
    p2 = Player(input('Player 2, please enter your name: '))
else:
    print('Invalid Choice, try again')
    choice = input('Would you like to play against a smart AI, a dumb AI, or another human? (1, 2, 3): ')

g = Gameplay()
play(g, p1, p2, print_game=True)
