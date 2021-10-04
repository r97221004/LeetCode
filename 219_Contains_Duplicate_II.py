# 時間複雜度: O(n)
# 空間複雜度: O(n)
# 使用 enumerate() 可以寫得更簡化，但為了跟之前的寫法保持一致，先這樣處理!
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        data = {}
        for i in range(len(nums)):
            if nums[i] not in data:
                data[nums[i]] = i
            else:
                if abs(data[nums[i]] - i) <= k:
                    return True
                else:
                    data[nums[i]] = i
        return False

p = Solution()
print(p.containsNearbyDuplicate([1,2,3,1,2,3], 2))