# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def twoSum(self, numbers, target):
        data = {}
        
        for i, val in enumerate(numbers):
            if target - val not in data:
                data[val] = i + 1
                
            else:
                return [ data[target - val], i + 1]

p = Solution()
print(p.twoSum([2, 7, 11, 15], 9))