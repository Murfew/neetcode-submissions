import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        minHeap = []
        for n, f in freq.items():
            heapq.heappush(minHeap, (f, n))

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        res = []
        for (f, n) in minHeap:
            res.append(n)

        return res
