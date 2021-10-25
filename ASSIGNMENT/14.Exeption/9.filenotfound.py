try:
    fo = open("myfile.txt","rt")
    print("File opened")
except FileNotFoundError:
    print("File does not exist")
except:
    print("Other error")