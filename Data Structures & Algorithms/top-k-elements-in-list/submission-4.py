import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Build frequency map
        freq = Counter(nums)

        # Use a heap to get k elems
        heap = []

        for n, f in freq.items():
            heapq.heappush(heap, (f, n))

            if len(heap) > k:
                heapq.heappop(heap)

        

        res = []
        # Build solution array
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res