'''
Order list and swap element positions (even -> odd, odd -> even)
Input: nums = [5,4,2,3]
Output: [3,2,5,4]
Input: nums = [2,5]
Output: [5,2]
'''
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(1,len(nums), 2):
            nums[i], nums[i-1] = nums[i-1], nums[i]
        return nums
        
