numbers=input("Enter numbers").split(",")
numberTuple=tuple(numbers)

for i in numberTuple:
    if(int(i)%5==0):
        print(i)