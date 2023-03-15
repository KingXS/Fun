f = open("brute.txt",'w',encoding='utf-8')

x = "+"

for i in range(1,100):
    f.write(x + '\n')
    print(x)
    x = x + "+"
