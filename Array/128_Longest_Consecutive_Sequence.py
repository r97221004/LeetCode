# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def longestConsecutive(self, nums):
        numsSet = set(nums)
        longest = 0

        for n in numsSet:
            if (n - 1) not in numsSet:
                length = 0
                while n + length in numsSet:
                    length += 1

                longest = max(longest, length)

        return longest


p = Solution()
print(p.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
