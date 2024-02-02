#Input: nums = [1,1,1,2,2,3], k = 2
#Output: [1,2]

#Input: nums = [1], k=1
#Output: [1]

#Input: nums = [1,2], k=2
#Output: [1,2]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        heap = [(v,k) for (k,v) in counter.items()]
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        return [num for (freq, num) in heap]
        