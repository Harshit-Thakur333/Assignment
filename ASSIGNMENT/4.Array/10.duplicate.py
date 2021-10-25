arr=[1,2,1,3,4,5,2,6,6,4,8,4]
arr1=[]
for i in arr:
    if i not in arr1:
        arr1.append(i)
    else:
        print(i,end=' ')