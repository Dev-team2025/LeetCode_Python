
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




{
  "model":"deepseek-coder:6.7b",
  "prompt":"Write  about the college in 2 line",
  "stream":false
}
# http://host.docker.internal:11434/api/generate

# sheet 
# 1wKIox5v7gNLv536Wqmvt98uV6XMsym3QH62SWGvi_fs