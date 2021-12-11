# 時間複雜度: O(n**2), (n-1) + (n-2) + .... + 1 = n**2/2  -> O(n**2)
# 空間複雜度: O(1)
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

p = Solution()
print(p.twoSum([2, 7, 11, 15], 9))


# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def twoSum(self, nums, target):
        data = {}
        
        for i, val in enumerate(nums):
            if target - val not in data:
                data[val] = i
            else:
                return [i, data[target - val]]

p = Solution()
print(p.twoSum([2, 7, 11, 15], 9))
