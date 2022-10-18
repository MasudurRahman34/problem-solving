nums = [2, 7, 11, 15]
target = 9
dic_nums={}

# sloution 1
# dic_nums1={}
# for i in range(len(nums)):
#     dic_nums[nums[i]]=i
# for i, num in enumerate(dic_nums):
#     if (target-num) in dic_nums and i!=dic_nums[target-num]:
#         print([i,dic_nums[target-num]])

# solution 2

for i, v in enumerate(nums):
    if (target-v) in dic_nums:
        print([dic_nums[target-v],i])
    dic_nums[v]=i


