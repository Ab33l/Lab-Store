'''
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]
'''
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        newList = []
        for element in arr2:
            occurrences = arr1.count(element)
            newList.extend([element] * occurrences)
        
        if len(newList) == len(arr1):
            return newList
        else:
            missing_elements = [item for item in arr1 if arr1.count(item) > newList.count(item)]
            missing_elements.sort()
            return newList + missing_elements
        
