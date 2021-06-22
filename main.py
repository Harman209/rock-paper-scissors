import random

choices = ['r', 'p', 's']


player = input('Let\'s play rock paper scissors.\n \'r\' for rock, \'p\' for paper and \'s\' for scissors')
computer = random.choice(choices)

# r > s, s > p, p > r 

def result(computer, player):
    if computer == player:
        print('It is a tie!!')
    if (player == 'r' and computer == 's') and (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        print('You Won!!')
    
    else:
        print('You Lost :(')

if __name__ == '__main__':
    print('You played ' + player + ' computer played ' + computer)
    result(computer, player)
