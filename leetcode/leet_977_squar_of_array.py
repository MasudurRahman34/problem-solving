nums = [-7,-3,2,3,11]
result=[]
n=len(nums)
for i in range(0,n):
    r=nums[i]*nums[i]
    result.append(r)
result.sort()
print(result)