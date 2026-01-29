# 1480. Running Sum of 1d Array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return nums
    
obj=Solution()
res=obj.runningSum([12,3,21,2,4])
print(res)