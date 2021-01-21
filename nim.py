import random
names = open("names.txt", "r")
first_names = [line.split(" ")[0] for line in names]


class Player:
    def __init__(self, name):
        """Player Name"""
        self.human = name
    
    def get_move(self):
        return input("Input how many coins you'd like to take away: ")


class RandomComputerPlayer:
    def __init__(self):
        self.bot_name = random.choice(first_names)
        print(rf'You will be playing against {self.bot_name}')
        
    def get_move(self):
        return random.randint(1, 3)
    

class GeniusComputerPlayer:
    def __init__(self):
        self.bot_name = random.choice(first_names)
        print(rf'You will be playing against {self.bot_name}')

    def get_move(self):
        return random.randint(1, 3)



class Gameplay:
    def __init__(self):
        self.coins = 12
        self.taken = 0

    def print_coins(self):
        print(" o" * (self.coins - self.taken))


        

    
turn = 'p1'
def play(game, p1, p2, print_game):
    if print_game:
         game.print_coins()
    
    while game.coins > 0:
        if turn == 'p1':
            take_away = p1.get_move()
            print(take_away)


            turn == 'p2'
            
        else:
            take_away = p2.get_move()
        




    


        
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
