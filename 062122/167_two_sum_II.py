class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers)-1
        result = []

        while left < right:
            temp = numbers[left] + numbers[right]
            if temp < target:
                left += 1
            if temp > target:
                right -= 1
            if temp == target:
                result.append(left+1)
                result.append(right+1)
                return result
