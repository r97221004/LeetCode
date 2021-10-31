# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def countBinarySubstrings(self, s):
        s = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split(' ')))
        return   sum(  min(i, j )  for i, j in zip(s, s[1:])  )

p = Solution()
print(p.countBinarySubstrings("00110011"))