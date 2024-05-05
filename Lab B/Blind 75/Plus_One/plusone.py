#PlusOne
#Input: digits = [1,2,3]
#Output: [1,2,4]

#Input: digits = [9]
#Output: [1,0]

#Input: digits = [9,9]
#Output: [1,0,1,0]

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        one, i = 1,0
        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
            i += 1
        return digits[::-1] 
