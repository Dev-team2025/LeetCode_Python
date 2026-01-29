# 9. Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original = x
        rev = 0
        
        while x > 0:
            x %= 10
            rev = rev * 10 + x 
            x //= 10
        
        return original == rev
