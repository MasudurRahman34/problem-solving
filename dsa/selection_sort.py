
num=[5, 2, 6, 3, 4]

len= len(num)

for i in range(len-1):
    min=i
    for j in range(i+1,len):
        if num[j] < num[min] :
            min = j
    if min != i:
        temp=num[i]
        num[i]=num[min]
        num[min]=temp;
print(num)



