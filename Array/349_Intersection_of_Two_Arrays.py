# 時間複雜度: O(n + m), n = len(nums1) 且 m = len(nums2)
# 空間複雜度: O(n + m)
# 注意像 set1 = set(nums1) 這種把列表轉集合的操作時間複雜度是: O(n)
class Solution:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)
p = Solution()
print(p.intersection([1, 2, 2, 1], [2, 2]))


# 時間複雜度: O(n + m), n = len(nums1) 且 m = len(nums2)
# 空間複雜度: O(n + m)
class Solution:
    def intersection(self, nums1, nums2):
        res = set()
        nums2 = set(nums2)
        for i, val in enumerate(nums1):
            if val in nums2 and val not in res:
                res.add(val)
                
        return res

p = Solution()
print(p.intersection([1, 2, 2, 1], [2, 2]))