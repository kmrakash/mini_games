from PIL import Image
import time
import random

def show_board():
    im = Image.open('snake.jpeg','r')
    im.show()

def check_ladders(point):
    if point == 4:
        print('Ladder')
        return 14
    elif point == 9:
        print('Ladder')
        return 31    
    elif point == 20:
        print('Ladder')
        return 38
    elif point == 28:
        print('Ladder')
        return 84
    elif point == 40:
        print('Ladder')
        return 59
    elif point == 63:
        print('Ladder')
        return 81
    elif point == 71:
        print('Ladder')
        return 91
    else:
        return point

def check_snake(point):
    if point == 17:
        print('Snake')
        return 7
    elif point == 54:
        print('Snake')
        return 34
    elif point == 64:
        print('Snake')
        return 60
    elif point == 87:
        print('Snake')
        return 24
    elif point == 93:
        print('Snake')
        return 73
    elif point == 96:
        print('Snake')
        return 75
    elif point == 99:
        print('Snake')
        return 78
    else:
        return point

def reached(point):
    if point == 100:
        return True
    else:
        return False       


def play():
    p_1 = input('Player 1 , Enter Your Name: ')
    p_2 = input('Player 2, Enter Your Name: ')
    point_1 = 0
    point_2 = 0
    end = 100
    turn = 0
    while(1):
        if turn%2 == 0:
            print(p_1 , 'Your Turns')
            c=int(input('press 1 to continue and 0 to quit the game '))
            if c == 0:
                print(p_1 , 'You Quit the Game ')
                print(p_1  + ' SCORED ' + str(point_1))
                print(p_2 + ' SCORED ' + str(point_2))
                break
            else:
                print("Dice is Rolling...")
                time.sleep(2)
                dice = random.randint(1,6)
                print('Dice Score ' + str(dice))
                print()
                current = point_1
                point_1 += dice
                point_1 = check_ladders(point_1)
                point_1 = check_snake(point_1)
                if point_1 > end:
                    point_1 = current
                    print("End limit exceed, No movement wait for next Try " + str(point_1))
                if reached(point_1):
                    print(p_1 + ' Congratulations You Won!!!')
                    break
                print(p_1 + ' You are at ' + str(point_1))    
                print()                                                                                            #for new line

        else:
            print(p_2 , 'Your Turns')
            print()                                                                                                #for new line
            c=int(input('press 1 to continue and 0 to quit the game '))
            if c == 0:
                print(p_2 , 'You Quit the Game ')
                print(p_1  + ' SCORED ' + str(point_1))
                print(p_2 + ' SCORED ' + str(point_2))
                break
            else:
                print("Dice is Rolling...")
                time.sleep(2)
                dice = random.randint(1,6)
                print('Dice Score ' + str(dice))
                print()                                                                                      #for new line
                current = point_2
                point_2 += dice
                point_2 = check_ladders(point_2)
                point_2 = check_snake(point_2)
                if point_2 > end:
                    point_2 = current
                    print("End limit exceed, No movement wait for next Try " + str(point_2))
                if reached(point_2):
                    print(p_2 + ' Congratulations You Won!!!')
                    break
                print(p_2 + ' You are at ' + str(point_2)) 
                print()                                                                                   #for new line
        turn += 1                  


show_board()
play()

            

