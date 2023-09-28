class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newlist = set()
        for x in nums:
            if x in newlist:
                return True
            newlist.add(x)
        return False