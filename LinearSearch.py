
myList = [27,19,23,32,84,2,55,14,16,42]

ub = 9
lb = 0 
top = ub 
Swap = True

while Swap and top > lb:
    Swap = False
    for x in range (lb,top):
        if myList[x] > myList[x+1]:
            temp=myList[x]
            myList[x] = myList[x+1]
            myList[x+1]=temp
            Swap = True
    top = top-1
print(myList)
