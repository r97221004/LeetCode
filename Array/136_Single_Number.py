# Bit Manipulation
# 時間複雜度: O(n)
# 空間複雜度: O(1)
# 概念: a^0 = a 且 a^a = 0 且 a^b^a = a^a^b = 0^b = b 
class Solution:
    def singleNumber(self, nums):
        res = 0
        for i in nums:
            res ^= i
        return res
p = Solution()
print(p.singleNumber( [4, 1, 2, 1, 2]))    

# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def singleNumber(self, nums):
        data = {}
        for i in nums:
            data[i] = data.get(i, 0) + 1
        for i in data.keys():
            if data[i] == 1:
                return i
p = Solution()
print(p.singleNumber([4, 1, 2, 1, 2]))   