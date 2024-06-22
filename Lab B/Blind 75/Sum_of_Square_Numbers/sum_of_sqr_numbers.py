'''
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Input: c = 3
Output: false

Given a non-negative integer c, decide whether there're two integers a and b such that a^2 + b^2 = c.
'''
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))
        while left <= right:
            if left * left + right * right == c:
                return True
            elif left * left + right * right > c:
                right -= 1
            else:
                left += 1
        return False
