'''
Input: nums = [2,1,3,2,1]

Output: 3

Explanation:

One of the optimal solutions is to remove nums[0], nums[2] and nums[3].

Input: nums = [1,3,2,1,3,3]

Output: 2

Explanation:

One of the optimal solutions is to remove nums[1] and nums[2].

Input: nums = [2,2,2,2,3,3]

Output: 0

Explanation:

nums is already non-decreasing.
'''
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
    
        # Initialize the dp array
        dp = [1] * n
    
        # Fill dp array with LNDS lengths
        for i in range(1, n):
            for j in range(i):
                if nums[j] <= nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
    
        # The length of the longest non-decreasing subsequence
        length_of_lnds = max(dp)
    
        # Minimum number of deletions required
        return n - length_of_lnds
        
