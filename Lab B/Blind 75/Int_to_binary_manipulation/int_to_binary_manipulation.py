'''
Convert int to binary, determine total number of 1 bits, print positions the 1 bits appear in the binary
'''
class Solution:
    def intManipulation(self, s: int) -> list:
       binaryValue = ''
       finalList = []
       while s > 0:
          binaryValue = str(s%2) + binaryValue
          s = s // 2
       numberOfones = sum([1 for x in binaryValue if c == '1'])
       finalList.append(numberOfones)
       for index, value in enumerate(binaryValue):
          if value == '1':
             finalList.append(index+1)
       return finalList
