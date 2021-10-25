try:
     raise ValueError("I have raised an Exception")
except ValueError as exp:
     print ("Error", exp)     
try:
     raise ValueError
except ValueError as exp:
     print ("Error", exp)     