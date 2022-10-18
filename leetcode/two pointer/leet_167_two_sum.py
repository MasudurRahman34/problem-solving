numbers = [2,7,11,15]
target = 9
n=len(numbers)
i=0
j=n-1
rarray=[]
while i <= j:
    result=numbers[i]+numbers[j]
    if result==target :
        rarray+=[(i+1),(j+1)]
        print(rarray)
        break
    if result > target:
        j-=1
    elif result < target :
        i+=1
