class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        #print(target)
        for i in range(len(nums)):
            d[nums[i]] = i
        for j in range(len(nums)):
            t = target - nums[j]
            #print(t)
            if t in d and d[t]!=j:
                return [j, d[t]]

        
