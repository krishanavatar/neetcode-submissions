from collections import defaultdict 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)[:k]
        return [i[0] for i in counter]
        