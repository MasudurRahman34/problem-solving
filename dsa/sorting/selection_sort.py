nums = [8,-3,2,4,1]
len=len(nums)
for i in range(len):
    min_index=i
    for j in range(i+1,len):
        # print(nums[j],nums[min_index], nums[i])
        if nums[j] < nums[min_index] :
            print(nums[j], nums[min_index], nums[i])
            min_index=j
    temp=nums[i]
    nums[i]=nums[min_index]
    nums[min_index]=temp
print(nums)