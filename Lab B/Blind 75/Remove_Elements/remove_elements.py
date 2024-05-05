Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        numberOfTimes = 0
        for x in range(len(nums)):
            if nums[x] != val:
                nums[numberOfTimes] = nums[x]
                numberOfTimes += 1
        return numberOfTimes
