class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If x is negative or ends with 0 but not 0 itself, it's not a palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # Initialize reversed number
        reversed_num = 0
        
        # Reverse half of the number and compare
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        # If the length of x is odd, we need to handle the middle digit
        # For example, if the original number is 12321, at the end of the loop, x will be 12 and reversed_num will be 123.
        # So, we need to remove the last digit of reversed_num to handle the middle digit.
        return x == reversed_num or x == reversed_num // 10
