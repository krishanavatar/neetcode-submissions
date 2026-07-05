from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}

        for inx, num in enumerate(nums):
            diff = target - num
            if diff in counter:
                diff_inx = counter[diff]
                return [diff_inx, inx]
            counter[num] = inx
            
            
                


        