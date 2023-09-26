num_input = input("Your Input : ")
n, i, j = num_input.split()
n = int(n)
i = int(i)
j = int(j)
for x in range(1,n+1):
    if x%i == 0 and x%j == 0 :
        print(x,"Ping Pong")
    elif  x%i == 0 :
        print(x,"Ping")
    elif  x%j == 0 :
        print(x,"Pong")
    else :
        continue