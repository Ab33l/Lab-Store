'''
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        start = 0
        max_length = 0
    
        for i, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= start:
                # Move the start right after the last occurrence of the current character
                start = char_index_map[char] + 1
            # Update the latest index of the character
            char_index_map[char] = i
                # Calculate the length of the current substring and update max_length
            max_length = max(max_length, (i - start) + 1)
    
        return max_length


        
