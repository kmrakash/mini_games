n = int(input())
magic_square = []
for i in range(n):
    l = []
    for j in range(n):
        l.append(0)
    magic_square.append(l) 

i = n//2
j = n-1
count = 1
num = n*n
while(count<=num):
    if(i == -1 and j == n):
        j = n-2
        i = 0
    else:
        if(j==n):
            j = 0
        if(i <0):
            i = n-1    
    if(magic_square[i][j] !=0):
        j = j-2
        i = i+1
        continue
    else:
        magic_square[i][j] = count
        count += 1                
    i= i - 1
    j = j + 1
for i in range(n):
    for j in range(n):
        print(magic_square[i][j], end =" ")
    print()

print("The sum of any row/column/diagonal must: " + str((n*(n*n + 1))/2) )                   