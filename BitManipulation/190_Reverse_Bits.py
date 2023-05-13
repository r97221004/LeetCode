# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def reverseBits(self, n):
        result = 0

        for i in range(32):
            tmp = n % 2
            result = result | (tmp << 31 - i)
            n = n >> 1
        return result


# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(31, -1, -1):
            res += n % 2*(2**i)
            n = n >> 1

        return res
