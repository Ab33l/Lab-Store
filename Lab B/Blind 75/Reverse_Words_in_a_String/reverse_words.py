'''
Input: s = "the sky is blue"
Output: "blue is sky the"
Input: s = "a good   example"
Output: "example good a"
Input: s = "  hello world  "
Output: "world hello"
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.lstrip().rstrip()
        word_list = [word for word in s.split(" ") if word != ""][::-1]
        result_string = " ".join(word_list)
        return result_string
