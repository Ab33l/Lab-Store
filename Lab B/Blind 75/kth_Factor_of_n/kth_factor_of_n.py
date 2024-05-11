'''
Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
Input: n = 7, k = 2
Output: 7
Explanation: Factors list is [1, 7], the 2nd factor is 7.
Input: n = 4, k = 4
Output: -1
Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.
'''
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        finalValue = []
        for x in range(1,n+1):
            if n%x == 0:
                finalValue.append(x)
        if len(finalValue) < k:
            return -1
        else:
            return finalValue[k-1]
