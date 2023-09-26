arrInput = input("Your Input : ")
charInput = input("Char : ")
ls = arrInput.split(", ")
texts = []
num = []
i = 0

result = [ls[i] for i in range(len(ls)) if i == ls.index(ls[i]) ]

        
for x in result:
    x2 = x.lower()
    charInput = charInput.lower()
    try:
        index = x2.index(charInput)
        i = i+1
        texts.append(x)
        num.append(index)
    except ValueError:
        continue

if i>0 :
    print(texts)
    print(num)
else :
    print("No results found")
