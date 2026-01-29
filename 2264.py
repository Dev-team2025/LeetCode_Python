class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        for d in "9876543210":
            if d*3 in num:
                return d*3
        return ""


''' class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                res = max(res, num[i:i+3])
        return res
# '''
# How max() works for strings

# In Python, strings are compared lexicographically
# → character by character using their ASCII / Unicode values.