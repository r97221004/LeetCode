
# 兩個迴圈的暴力法: 時間複雜度 (n-1) + (n-2) + .... + 1 = n**2/2  -> O(n**2)
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

p = Solution()
print(p.twoSum([2, 7, 11, 15], 9))


# 字典法: 時間複雜度 O(n)
class Solution:
    def twoSum(self, nums, target):
        my_dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in my_dict:
                my_dict[nums[i]] = i
            else:
                return [my_dict[target - nums[i]], i]

p = Solution()
print(p.twoSum([2, 7, 11, 15], 9))
