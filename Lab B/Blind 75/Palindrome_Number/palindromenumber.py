#Input: x = 121
#Output: True, 121 = 121

#Input: x = -121
#Output: False, 121- != 121

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        div = 1
        while x >= 10 * div:
            div *= 10

        while x:
            right = x % 10
            left = x // div

            if left != right: return False

            x = (x % div) // 10
            div = div / 100
        return True
