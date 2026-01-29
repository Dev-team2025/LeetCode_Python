
# 217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False


'''class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            if nums.count(i) >= 2:
                return True
        return False
'''

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return len(nums) != len(set(nums))

