import random
print("LET'S PLAY MONTE HALL GAME ")
print("YOU HAVE THREE DOORS NAMED 0,1,2 \n CHOOSE ANY ONE \n ONE OF DOOR CONTAINS BMW CAR \n ONE OF DOOR WILL OPENED AND ASK TO SWAP YOUR CHOICE")
print("Try your luck")    
doors = [0]*3
doors_goat = [0]*2
swap = 0
dont_swap = 0
j = 0
n = int(input("Enter Number of Test Cases: "))
while(j <= n):
    x = random.randint(0,2)
    doors[x] = "BMW"
    for i in range(0,3):
        if(i == x):
            continue
        else:
            doors[i] = "Goat"
            doors_goat.append(i)
    choice = int(input("Enter your choice: "))
    doors_open = random.choice(doors_goat)
    while(doors_open == choice):
        doors_open = random.choice(doors_goat)
    print("Door opened: "+str(doors_open))
    ch = input("Do you want to swap your choice y/n : ")
    if(ch == 'y'):
        if(doors[choice]=='Goat'):
            print("You Won BMW")
            print("BMW was in door number: " + str(x))
            swap += 1
        else:
            print("Better Luck Next Time")
    if(ch == 'n'):
        if(doors[choice]=='Goat'):
            print("BETTER LUCK NEXT TIME")
        else:
            print("YOU WON BMW")
            print("BMW was in door number: " + str(x))
            dont_swap += 1
    j += 1
print("TOTAL WINS ON SWAPPING: " + str(swap))
print("TOTAL WINS WITHOUT SWAPPING: " + str(dont_swap)) 
if swap > dont_swap:   
    print("AFTER PLAYING THE GAME YOU WILL REALISE DUE TO SWAPPING YOUR CHOICE, YOU HAVE A BETTER CHANCES OF WINS ")                           