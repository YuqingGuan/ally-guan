class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # two pointers
        i = 0

        result = []
        nums.sort()
        #print(nums)
        while i<len(nums)-1 and nums[i] <= 0:
            j = i+1
            k = len(nums)-1

            while j<k:
                if nums[j] + nums[k] > -nums[i]:
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j<k and nums[j]==nums[j-1]:
                        j += 1
            i += 1
            while i<j and nums[i]==nums[i-1]:
                i += 1

        return result

                
