arr = []
n = int(input("Enter the number : "))
for i in range(0,n):
    num = int(input())
    arr.append(num)
print(arr)
exists = int(input("Enter the number:")) in arr
num = int(input("Enter the number:")) in arr
print(exists)
print(num)
