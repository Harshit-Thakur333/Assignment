arr = []
n = int(input("Enter the number : "))
for i in range(0,n):
    num = int(input())
    arr.append(num)
print(arr)
print("Index of the number is:",arr.index(int(input())))