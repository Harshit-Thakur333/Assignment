num = int(input(" Please Enter the Maximum number : "))
 
number = 10
 
while number <= num:
    if(number % 2 == 0):
        print("{0}".format(number))
    number = number + 1