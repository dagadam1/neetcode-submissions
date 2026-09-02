class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        freq = [[] for _ in range(len(nums))]
        for n, f in c.items():
            freq[f-1].append(n)
        res = []
        for l in freq[::-1]:
            for n in l:
                res.append(n)
                if len(res) == k:
                    return res
