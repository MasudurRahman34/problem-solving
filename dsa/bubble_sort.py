def butbleSort(a:list):
    for i in range(len(a)):
        for j in range(0,len(a)-i-1):
            if a[j] > a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    return a

a=[0,-1, 3, 5, 9, 12]
n=len(a)
print(butbleSort(a))


