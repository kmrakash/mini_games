import string
import random
symbol = []
symbol = list(string.ascii_letters)
card_1 = [0]*5
card_2 = [0]*5
pos_1 = random.randint(0,4)
pos_2 = random.randint(0,4)
same_symbol = random.choice(symbol)
symbol.remove(same_symbol)

card_1[pos_1] = same_symbol
card_2[pos_2] = same_symbol
i = 0
while(i < 5):
    if i != pos_1:
        card_1[i] = random.choice(symbol)
        symbol.remove(card_1[i])
    if i != pos_2:    
        card_2[i] = random.choice(symbol)
        symbol.remove(card_2[i]) 
    i += 1
print(*card_1,sep = '')
print(*card_2, sep = '')  
ch = input("Enter The similar one : ")
if ch == same_symbol:
    print("CORRECT " + str(ch))
else:
    print("Try Once More \nSame symbol is " + str(same_symbol))    
