#Input: s = "()"
#Output: true

#Input: s = "()[]{}"
#Output: true

#Input: s = "(]"
#Output: false

class Solution:
    def isValid(self, s: str) -> bool:
        stacklist = []
        closeToOpen = {"}":"{","]":"[",")":"("}
        for c in s:
            if c in closeToOpen:
                if stacklist and stacklist[-1] == closeToOpen[c]:
                    stacklist.pop()
                else:
                    return False
            else:
                stacklist.append(c)
        return True if not stacklist else False


        