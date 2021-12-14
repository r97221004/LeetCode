# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def numIdenticalPairs(self, nums):
        count = {}
        res = 0
        
        for i in nums:
            count[i] = count.get(i, 0) + 1
            
        for i in count.values():
            if i >=2:
                res += i*(i - 1)/2
        
        return res

p = Solution()
print(p.numIdenticalPairs([1, 2, 3, 1, 1, 3]))