class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)

        if number == number[::-1]:
            return True
        else:
            return False
        
# str[::-1] to reverse