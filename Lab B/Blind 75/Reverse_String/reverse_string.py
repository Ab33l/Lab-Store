'''
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Iterate over the first half of the list (up to the middle element) using the range range(len(s)//2).
In each iteration, it swaps the elements at indices i and ~i (which is the corresponding index from the end of the list).
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead in O(1).
        """
        for i in range(len(s)//2):
            s[i], s[~i] = s[~i], s[i]
        
