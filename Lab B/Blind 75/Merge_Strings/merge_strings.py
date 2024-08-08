'''
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        finallength = max(len(word1), len(word2))
        newstring = ""
        for x in range(finallength):
            if x < len(word1):
                newstring += word1[x]
            if x < len(word2):
                newstring += word2[x]
        return newstring
