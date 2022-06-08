class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)

        for s in strs:
            s1 = sorted(s)
            s2 = ''.join(s1)
            dic[s2].append(s)

        return dic.values()

#         alp = [0] * 26
#         dic = collections.defaultdict(list)
#         for s in strs:
#             n = [0] * 26
#             for l in s:
#                 n[ord(l)-ord('a')] += 1

#             dic[tuple(n)].append(s)

#         return dic.values()
        
