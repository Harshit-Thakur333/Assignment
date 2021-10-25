max=int(input("Please enter any maximum value"))
num=1
while num<=max:
    if(num%2!=0):
        print(num,"is odd")
    else:
        print(num,"is even")
    num=num+1