dict = {"Ridhi":"101","Shital":"102","Harshit":"103","Shruti":"104","Tannu":"105"}
dict["Gopal"] = "106" # 1.1
print(dict)
name = {"Aditya":"107"} # 1.2
dict.update(name)
print(dict)
access = dict["Ridhi"] # 1.3
print(access)
del dict["Tannu"] # 1.7
print(dict)
