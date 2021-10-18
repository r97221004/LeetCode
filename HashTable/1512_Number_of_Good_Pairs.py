# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def numIdenticalPairs(self, nums):
        data = {}
        result = 0
        for i in nums:
            data[i] = data.get(i, 0) + 1
            
        for key, val in data.items():
            if val >= 2:
                result += val*(val - 1)//2
        
        return result

p = Solution()
print(p.numIdenticalPairs([1,2,3,1,1,3]))