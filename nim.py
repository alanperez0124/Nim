import random

# Opening the names.txt file for the random bots
names = open("names.txt", "r")
first_names = [line.split(" ")[0] for line in names]


class Player:
    def __init__(self, name):
        """Assign the player a name"""
        self.name = name

    def get_move(self, coins, name):
        """Asks player for input and checks to see if move is valid"""
        valid_move = False
        enough_coins = False
        while not valid_move or not enough_coins:
            val = input(f"{name} takes: ")
            try:  # to make sure the value is 1, 2 or 3
                if int(val) not in range(1, 4):
                    raise ValueError
                else:
                    valid_move = True  
                    try:  # to make sure there are enough coins
                        if int(val) > coins:
                            raise PermissionError
                        else:
                            enough_coins = True

                    except PermissionError:
                        print('Not enough coins, please input appropriate amount.')
            except ValueError:
                print('Invalid input, please input 1, 2 or 3.')

        return val


class RandomComputerPlayer:
    def __init__(self):
        """Gives the random bot a name from list"""
        self.name = random.choice(first_names)


    def get_move(self, coins, name):
        """Ensures that random move is valid and returns move"""
        valid_move = False
        while not valid_move:
            x = random.randint(1, 3)
            if x <= coins:
                print(f"{name} takes {x}")
                val = True
                return x



class GeniusComputerPlayer:
    def __init__(self):
        self.name = random.choice(first_names)
        print()

    def get_move(self, coins, name):
        if coins % 4 == 3:
            print(f"{name} takes 3")
            return 3
        elif coins % 4 == 2:
            print(f"{name} takes 2")
            return 2
        elif coins % 4 == 1:
            print(f"{name} takes 1")
            return 1


class Gameplay:
    def __init__(self):
        self.coins = 12
        self.current_winner = None  # Keeping track of the winner

    def print_coins(self):
        print(" o" * self.coins, '\n')


def play(game, p1, p2, print_game):
    print(f'Starting game: {p1.name} vs. {p2.name}')

    if print_game:
        game.print_coins()

    turn = 'p1'

    while game.coins > 0:
        if turn == 'p1':
            take_away = p1.get_move(game.coins, p1.name)
            # print(rf'{p1.name} took {take_away} coins')

        else:
            take_away = p2.get_move(game.coins, p2.name)
            # print(rf'{p2.name} took {take_away} coins')

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
        print(f'{p2.name.upper()} WINS!')


# Main body of code
print('If you\'d like to watch two robots go at it, please type \'4\' when prompted for number.')
choice = input('Would you like to play against a smart AI, a random bot, or another human? (1, 2, 3): ')
print()
if choice == '1':
    p1 = Player(input('Player 1, please enter your name: '))
    p2 = GeniusComputerPlayer()
elif choice == '2':
    p1 = Player(input('Player 1, please enter your name: '))
    p2 = RandomComputerPlayer()
elif choice == '3':
    p1 = Player(input('Player 1, please enter your name: '))
    p2 = Player(input('Player 2, please enter your name: '))
elif choice == '4':
    p1 = RandomComputerPlayer()
    p2 = RandomComputerPlayer()
else:
    print('Invalid Choice, try again')
    choice = input('Would you like to play against a smart AI, a dumb AI, or another human? (1, 2, 3): ')

g = Gameplay()
play(g, p1, p2, print_game=True)