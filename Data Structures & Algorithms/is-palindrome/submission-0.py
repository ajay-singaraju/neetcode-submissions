class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(char.lower() for char in s if char.isalnum())

        def helper(left: int, right: int) -> bool:
            if left >= right:
                return True
            
            if s[left] != s[right]:
                return False
            
            return helper(left + 1, right - 1)
        

        return helper(0, len(s) - 1)

    