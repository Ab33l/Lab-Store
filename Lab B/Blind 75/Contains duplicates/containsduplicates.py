#Input => nums = [1,1,1,3,3,4,3,2,4,2]
#Output => true


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newlist = set()
        for x in nums:
            if x in newlist:
                return True
            newlist.add(x)
        return False