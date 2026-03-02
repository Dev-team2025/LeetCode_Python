
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
    
# if the stament not used then it itterates till the len of the string
# for i in s:
#     if i==" ":
#         print(s.split()[-1])



