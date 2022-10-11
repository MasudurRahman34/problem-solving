class Solution:
    nums = [1, 3, 5, 6]
    target = 7
    def searchInsert(self, nums: list[int], target: int) -> int:
        n=len(nums)
        left=0
        right=n-1
        while(left <= right) :
            mid = (left+right)//2
            if (nums[mid] == target):
                return(mid)
            elif(target > nums[mid]) :
                left= mid+1
            else :
                right=mid-1
        return left
result= Solution().searchInsert(Solution.nums, Solution.target)
print(result)

