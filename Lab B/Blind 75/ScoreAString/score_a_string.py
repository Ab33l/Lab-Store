'''
Given a string, find the absolute sum of the ascii difference each of the adjascent characters, used two pointer approach
Input: s = "hello"
Output: 13
Explanation:
The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

Input: s = "zaz"
Output: 50
Explanation:
The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.
'''
class Solution:
    def scoreOfString(self, s: str) -> int:
        finalSum = 0
        startPointer = 0
        nextPointer = 1
        while nextPointer <= len(s) - 1:
            finalSum += abs(ord(s[startPointer]) - ord(s[nextPointer]))
            startPointer += 1
            nextPointer += 1
        return finalSum
        
