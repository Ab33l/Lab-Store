'''
Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
'''
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        finalValue = 0
        for x in arr:
            if x%2 != 0:
                finalValue += 1
            else:
                finalValue = 0
            if finalValue == 3:
                return True
        return False
