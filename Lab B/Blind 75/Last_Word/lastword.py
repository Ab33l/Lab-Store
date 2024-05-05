#Length of Last Word
#Example 1
#Input: s = "Hello World"
#Output: 5

#Example 2
#Input: s = "   fly me   to   the moon  "
#Output: 4

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stringList = s.split()
        return len(stringList[-1])
