'''
An array is special if its adjascent elements have different parity (one is odd and one is even) i.e [1,2,3,4] -> (1,2),(2,3),(3,4)
Input: nums = [1] 
Output: true (only has one element)
Input: nums = [2,1,4] -> (2,1) and (1,4) have different parity
Output: true
Input: nums = [4,3,1,6] -> (4,3) have different parity, (3,1) have same parity 
Output: false
'''
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        startPointer = 0
        nextPointer = 1
        if len(nums) == 1:
            return True
        while nextPointer <= len(nums) - 1:
            if (nums[startPointer] % 2 == 0 and nums[nextPointer] % 2 != 0) or (nums[startPointer] % 2 != 0 and nums[nextPointer] % 2 == 0):
                startPointer = startPointer + 1
                nextPointer = nextPointer + 1
                continue
            else:
                return False
        return True

        
