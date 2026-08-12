class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Get a counter for the items in the list
        # return the k first keys when sorted by values in desc

        counter = Counter(nums)
        sorted_by_value = sorted(counter.items(), key=lambda x: x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_by_value[i][0])

        return res