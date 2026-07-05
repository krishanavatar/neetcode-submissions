from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = defaultdict(list)
        # for inx, num in enumerate(nums):
            
        for inx, num in enumerate(nums):
            diff = target - num
            if diff in counter:
                diff_inx = [i for i in counter[diff] if i != inx]
                if len(diff_inx) > 0:
                    return sorted([inx, diff_inx[0]])

            counter[num].append(inx)
            
            
                


        