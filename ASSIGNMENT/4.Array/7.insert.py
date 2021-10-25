arr = [1,2,3,4,5,6,7]
element = int(input("Enter the num :"))
insert_element = int(input("Which element before:"))
index = arr.index(insert_element)
arr.insert(index , element)
print(arr)