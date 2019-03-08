import string
dict = {}
data = ""
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]] = string.ascii_letters[i - 5]
print(dict) 
X = open("test.txt",'r',encoding = 'utf-8')  
print(X.read()) 
print("After encoding the letter in different manner ")
file = open("encoded.txt",'w',encoding = 'utf-8')
with open("test.txt") as f:
    while True:
        c = f.read(1)
        if not c:
            print("ENd OF THE FILE")
            break
        if c in dict:
            data = dict[c]
        else:
            data = c
        file.write(data)
file.close()            
      
