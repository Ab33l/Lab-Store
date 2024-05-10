'''
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
Input: flowerbed = [0,1,0]
Output: false
'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            #check if current element is 0 and (is the first element or previous element is 0) and (is the last element or next element is zero)
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False
        
        
