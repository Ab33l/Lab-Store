'''
Checks if there exists a one-to-one mapping between characters in s and characters in t.
Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        shm = {}
        thm = {}
        for i in range(len(s)):
            if not shm.get(s[i]):
                shm[s[i]] = t[i]
            if not thm.get(t[i]):
                thm[t[i]] = s[i]
            if shm[s[i]] != t[i] or thm[t[i]] != s[i]:
                return 0
        return 1

        
