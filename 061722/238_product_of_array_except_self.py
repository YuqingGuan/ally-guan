class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l = len(nums)
        res = [1]*l

        for i in range(1,l):
            res[i] = res[i-1]*nums[i-1]

        init = 1

        for j in reversed(range(l)):
            res[j] = res[j] * init
            init = init * nums[j]

        return res
            
