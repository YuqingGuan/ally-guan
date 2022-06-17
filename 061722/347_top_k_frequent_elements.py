from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        res = heapq.nlargest(k, hashmap, key=hashmap.get)
        # print(res)
        return res
