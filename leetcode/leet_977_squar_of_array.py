nums = [-7,-3,2,3,11]
result=[]
n=len(nums)
for i in range(0,n):
    r=nums[i]*nums[i]
    result.append(r)
# result.sort()
# for i in range(n):
#     min_index=i
#     for j in range(i+1,n):
#         if(result[j] < result[min_index]):
#             min_index = j
#     temp = result[i]
#     result[i]=result[min_index]
#     result[min_index]=temp

print(result)