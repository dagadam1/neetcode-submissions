class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = dict()
        for i, x in enumerate(nums):
            indices[x] = i
        for i, x in enumerate(nums):
            if j := indices.get(target - x):
                if j != i:
                    return [i, j]
