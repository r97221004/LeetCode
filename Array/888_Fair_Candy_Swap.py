# 時間複雜度 O(n + m), n = len(aliceSizes) 且 m = len(bobSizes)
# 空間複雜度: O(m)
# 注意注意! x in list 時間複雜度: O(n); x in set 時間複雜度: O(1); x in dict 時間複雜度: O(1)
# A - i + j = B - j + i
# j = (B - A)/2 + i 
class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        diff = sum(bobSizes) - sum(aliceSizes)
        setB = set(bobSizes)
        
        for i, val in enumerate(aliceSizes):
            if val + diff/2 in setB:
                return [val, val + diff/2]

p = Solution()
print(p.fairCandySwap([1, 1], [2, 2]))