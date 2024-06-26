'''
Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

Input: nums = [0,0]
Output: -1
Explanation: No numbers fit the criteria for x.
If x = 0, there should be 0 numbers >= x, but there are 2.
If x = 1, there should be 1 number >= x, but there are 0.
If x = 2, there should be 2 numbers >= x, but there are 0.
x cannot be greater since there are only 2 numbers in nums.

Input: nums = [0,4,3,0,4]
Output: 3
Explanation: There are 3 values that are greater than or equal to 3.
'''
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        
        if nums[-1] > len(nums):
            return len(nums)
        
        if nums[0] == 0:
            return -1
        
        l = 0
        r = len(nums) - 1
        m = 0
        
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > m:
                l = m + 1
            elif nums[m] < m:
                r = m - 1
            else:
                return -1
        
        return m + 1 if nums[m] > m else m
