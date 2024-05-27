'''
Identify value of highest positive value with equal negative value in an array. Sorted the list then used two pointers
Input: nums = [-1,2,-3,3]
Output: 3
Explanation: 3 is the only valid k we can find in the array.

Input: nums = [-1,10,6,7,-7,1]
Output: 7
Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.

Input: nums = [-10,8,6,7,-2,-3]
Output: -1
Explanation: There is no a single valid k, we return -1.
'''

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        firstPointer = 0
        finalPointer = len(nums) - 1
        nums.sort()
        while firstPointer != finalPointer:
            result = nums[finalPointer] + nums[firstPointer]
            if result == 0:
                return nums[finalPointer]
            elif result > 0:
                finalPointer -= 1
            else:
                firstPointer += 1
        return -1    
