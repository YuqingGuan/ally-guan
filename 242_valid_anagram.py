class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = {}
        for i in s:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1

        for j in t:
            if j not in result:
                return False
            else:
                result[j] -=1

        return not (any(result.values())!=0)


          
