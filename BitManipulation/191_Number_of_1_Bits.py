# 時間複雜度: O(1) # The input must be a binary string of length 32.
# 空間複雜度: O(1)
class Solution:
    def hammingWeight(self, n):
        result = 0

        while n:
            result += n % 2
            n = n >> 1
        return result


p = Solution()
print(p.hammingWeight(n=11))
