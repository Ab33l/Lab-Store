'''
Input: s = "][]["
Output: 1
Explanation: You can make the string balanced by swapping index 0 with index 3.
The resulting string is "[[]]".

Example 2:
Input: s = "]]][[["
Output: 2
Explanation: You can do the following to make the string balanced:
- Swap index 0 with index 4. s = "[]][][".
- Swap index 1 with index 5. s = "[[][]]".
The resulting string is "[[][]]".

Example 3:
Input: s = "[]"
Output: 0
Explanation: The string is already balanced.
''' 
class Solution:
    def minSwaps(self, s: str) -> int:
        ans = 0
        for c in s:
            if c == '[':
                ans += 1
            elif ans > 0:
                ans -= 1
        return (ans + 1) // 2
