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
        prevMap = {}
        for i, value in enumerate(nums):
            diff = target - value
            if diff not in prevMap:
                prevMap[value] = i
            else:
                return [prevMap[diff], i]

        return []


p = Solution()
print(p.twoSum([2, 7, 11, 15], 9))
