class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        last = 1
        for i in nums:
            left.append(last*i)
            last = last*i
            
        right = []
        last = 1
        for i in reversed(nums):
            right.append(last*i)
            last = last*i
        right = list(reversed(right))
        
        res = []
        for i in range(len(nums)):
            if i==0:
                res.append(right[1])
            elif i==len(nums)-1:
                res.append(left[i-1])
            else:
                res.append(left[i-1]*right[i+1])
        return res
        