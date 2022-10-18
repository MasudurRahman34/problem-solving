nums = [3,3]
target = 6
rarray=[]
n=len(nums)
for i in range(0,n-1):
    for j in range(i+1, n):
        if(nums[i]+nums[j])==target :
            rarray += [(i), (j)]
            print(rarray)