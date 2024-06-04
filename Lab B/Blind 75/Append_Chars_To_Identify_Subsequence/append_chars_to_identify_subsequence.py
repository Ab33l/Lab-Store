'''
Input: s = "coaching", t = "coding"
Output: 4
Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
Now, t is a subsequence of s ("coachingding").
It can be shown that appending any 3 characters to the end of s will never make t a subsequence.

Input: s = "abcde", t = "a"
Output: 0
Explanation: t is already a subsequence of s ("abcde").
'''
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0  # Start both pointers at the beginning of s and t
        
        while i < len(s) and j < len(t):  # Continue until one of the strings is fully scanned
            if s[i] == t[j]:  # If characters match
                j += 1  # Move the pointer in t forward
            i += 1  # Always move the pointer in s forward
        
        return len(t) - j  # The number of characters in t not matched in s
        
