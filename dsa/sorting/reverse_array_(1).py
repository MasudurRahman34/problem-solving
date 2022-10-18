nums=["h","e","l","l","o"]
# use two pointer algorithm
left=0
right=len(nums)-1
while(left < right):
    temp=nums[left]
    nums[left]=nums[right]
    nums[right]=temp
    left+=1
    right-=1
print(nums)