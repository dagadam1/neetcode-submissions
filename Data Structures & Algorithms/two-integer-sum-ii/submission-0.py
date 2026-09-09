class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i < len(numbers) and j > 0:
            sm = numbers[i] + numbers[j]
            if sm < target:
                i += 1
            elif sm > target:
                j -= 1
            else:
                return [i+1, j+1]