# 時間複雜度: O(n)
# 空間複雜度: O(1)
# 注意: len() 的時間複雜度是 O(1), zip()  的時間複雜度也是 O(1)

class Solution:
    def isIsomorphic(self, s, t):
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

p = Solution()
print(p.isIsomorphic("egg", "add"))