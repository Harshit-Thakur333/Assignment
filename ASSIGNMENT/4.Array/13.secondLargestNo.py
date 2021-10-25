def second_largest(arr):
    large = max(arr)
    arr.remove(large)
    large = max(arr)
    print(large)
arr = []
n = int(input("Enter the number : "))
for i in range(0,n):
    num = int(input())
    arr.append(num)

print("2nd largest number in",arr,"is")
print(second_largest(arr))