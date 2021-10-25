arr= [12,17,34,37,60,65,67]
  
even_count, odd_count = 0, 0
  
for num in arr:
    if num % 2 == 0:
        even_count += 1
  
    else:
        odd_count += 1
          
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)