n = int(input("Your Input : "))
for x in range(1,n+1):
    if x%3 == 0 and x%5 == 0 :
        print(x,"Ping Pong")
    elif  x%3 == 0 :
        print(x,"Ping")
    elif  x%5 == 0 :
        print(x,"Pong")
    else :
        continue
   