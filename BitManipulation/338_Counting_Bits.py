# 時間複雜度: O(n)
# 空間複雜度: O(1)
# All whole numbers can be represented by 2N (even) and 2N + 1 (odd).
# For a given binary number, multiplying by 2 is the same as adding a zero at the end (just as we just add a zero when multiplying by ten in base 10).
# countBits(N) = countBits(2N)
# countBits(N) + 1 = countBits(2N + 1)
class Solution:
    def countBits(self, n):
        ans = [0]*(n + 1)

        for i in range(1, n + 1):
            ans[i] = ans[i//2] + i % 2

        return ans


p = Solution()
print(p.countBits(5))


# 時間複雜度: O(n•log(n))
# 空間複雜度: O(1)
class Solution:
    def countBits(self, n):
        result = []
        tmp = 0

        for i in range(n + 1):
            while i:
                tmp += i % 2
                i = i >> 1
            result.append(tmp)
            tmp = 0

        return result


p = Solution()
print(p.countBits(5))
