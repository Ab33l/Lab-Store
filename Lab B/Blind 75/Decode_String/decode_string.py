'''
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Input: s = "3[a2[c]]"
Output: "accaccacc"
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
'''
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString
