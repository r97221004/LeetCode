# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        data = {}
        
        for i, val in enumerate(nums):
            if val not in data: data[val] = i
            else:
                if i - data[val] <= k: return True
                data[val] = i    
            
        return False
        
p = Solution()
print(p.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))