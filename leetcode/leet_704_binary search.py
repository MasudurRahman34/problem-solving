
class Solution:
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while(left <= right) :
            mid = (left+right)//2
            if(nums[mid]==target) :
                return mid
            if(target > nums[mid]) :
                left=mid+1
            else:
                right=mid-1
        return -1
result= Solution().search(Solution.nums, Solution.target)
print(result)