# 時間複雜度: O(n + m), n = len(nums1) 且 m = len(nums2)
# 空間複雜度:O(min(n, m))

class Solution:
    def intersect(self, nums1, nums2):
        count = {}
        result = []
        
        for i in nums1:
            count[i] = count.get(i, 0) + 1
            
        for i in nums2:
            if i in count and count[i] > 0:
                result.append(i)
                count[i] -= 1
                
        return result

p = Solution()
print(p.intersect([1, 2, 2, 1], [2, 2]))