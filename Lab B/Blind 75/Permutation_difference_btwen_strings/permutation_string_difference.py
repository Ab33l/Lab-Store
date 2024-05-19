'''
Input: s = "abc", t = "bac"
Output: 2
Explanation: The permutation difference between element indices s and t is equal to |0 - 1| + |2 - 2| + |1 - 0| = 2
Input: s = "abcde", t = "edbac"
Output: 12
Explanation: The permutation difference between element indices s and t is equal to |0 - 3| + |1 - 2| + |2 - 4| + |3 - 1| + |4 - 0| = 12
'''
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        totalDifference = 0
        indexT = 0
        for x in range(len(s)):
            indexT = t.index(s[x])
            totalDifference = totalDifference + abs(x - indexT) 
        return totalDifference
        
