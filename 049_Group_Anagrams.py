# 時間複雜度: O(n*k*log(k)), n = len(strs) and k is the maximum length of a string in strs
# 空間複雜度: O(n*k)
class Solution:
    def groupAnagrams(self, strs):
        ans = {}
        for s in strs:
            key = tuple(sorted(s))
            ans[key] = ans.get(key, []) + [s]
        return list(ans.values())

p = Solution()
print(p.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))