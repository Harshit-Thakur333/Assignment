arr = []
n = int(input("Enter the number : "))
for i in range(0,n):
    num = int(input())
    arr.append(num)
print(arr)
arr.remove(int(input()))
print("After remove arr is :",arr)