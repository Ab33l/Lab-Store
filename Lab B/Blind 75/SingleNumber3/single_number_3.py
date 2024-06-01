'''
Uniquely identify elements in any order appearing once in a list with duplicate elements, used a list comprehension
Input: nums = [1,2,1,3,2,5]
Output: [3,5]

Input: nums = [-1,0]
Output: [-1,0]

Input: nums = [0,1]
Output: [1,0]
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        unique_elements = [item for item in nums if nums.count(item) == 1]
        return unique_elements
        
