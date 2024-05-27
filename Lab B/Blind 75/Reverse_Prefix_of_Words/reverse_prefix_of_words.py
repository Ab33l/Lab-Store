'''
Given a string and a character. Reverse the order of the section of the string till 1st occurrence of the character 
Input: word = "abcdefd", ch = "d"
Output: "dcbaefd"
Explanation: The first occurrence of "d" is at index 3. Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".

Input: word = "xyxzxe", ch = "z"
Output: "zxyxxe"
Explanation: The first and only occurrence of "z" is at index 3.
Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".

Input: word = "abcd", ch = "z"
Output: "abcd"
Explanation: "z" does not exist in word. You should not do any reverse operation, the resulting string is "abcd".
'''

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Find the index of the character 'ch' in the word
        ind = word.find(ch)
        if ind == -1:
            return word  # If character not found, return the original word
        
        # Reverse the prefix up to the index 'ind'
        prefix = word[:ind+1][::-1]
        
        # Append the remaining characters after 'ch'
        ans = prefix + word[ind+1:]
        
        return ans
        
