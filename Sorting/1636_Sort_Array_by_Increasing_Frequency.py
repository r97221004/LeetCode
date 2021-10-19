# 時間複雜度:O(nlog(n))
# 空間複雜度: O(n)
class Solution:
    def frequencySort(self, nums):
        count = {}        
        for i in nums:
            count[i] = count.get(i, 0) + 1         # count = collections.Counter(nums)
        
        return sorted(nums, key=lambda x: (count[x], -x))

p = Solution()
print(p.frequencySort([1,1,2,2,2,3]))