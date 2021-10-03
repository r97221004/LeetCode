# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def twoSum(self, numbers, target):
        data = {}
        for i in range(len(numbers)):
            if target - numbers[i] not in data:
                data[numbers[i]] = i + 1
            else:
                return [data[target - numbers[i]], i + 1 ]

p = Solution()
print(p.twoSum([2,7,11,15], 9))