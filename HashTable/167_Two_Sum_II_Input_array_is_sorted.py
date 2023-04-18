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



class Solution:
    def twoSum(self, numbers, target):
        prevMap = {}

        for i, value in enumerate(numbers):
            diff = target - value
            if diff in prevMap:
                return [prevMap[diff] + 1, i + 1]
            prevMap[value] = i

        return []


p = Solution()
print(p.twoSum([2, 7, 11, 15], 9))