# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def reverse(self, x):
        sign = 1 if x >= 0 else -1
        x = sign*int(str(abs(x))[::-1])

        return x if -2**31 <= x <= 2**31 - 1 else 0

p = Solution()
print(p.reverse(x = 123))