import random


def roll_dice(numbers=3, points=None):
    print('<<<<< ROLL THE DICE! >>>>>')
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1, 7)
        points.append(point)
        numbers = numbers - 1
    return points


def roll_result(total):
    isBig = 11 <= total <= 18
    isSmall = 3 <= total <= 10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'


def start_game():
    print('<<<<< GAME STARTS! >>>>>')
    choices = ['Big', 'Small']
    your_choice = input('Big or Small :')
    if your_choice in choices:
        points = roll_dice()
        total = sum(points)
        youWin = your_choice == roll_result(total)
        if youWin:
            print('The points are', points, 'You win !')
        else:
            print('The points are', points, 'You lose !')
        return youWin
    else:
        print('Invalid Words')
        start_game()


def start_game_with_bet():
    your_account = 1000
    while your_account > 0:
        your_bet = input('How much you wanna bet? - ')
        youWin = start_game()
        if youWin:
            your_account = your_account + int(your_bet)
            print('You gained ' + str(your_bet) + ', you have ' + str(your_account) + ' now')
        else:
            your_account = your_account - int(your_bet)
            print('You lost ' + str(your_bet) + ', you have ' + str(your_account) + ' now')
    print('GAME OVER')


start_game_with_bet()
