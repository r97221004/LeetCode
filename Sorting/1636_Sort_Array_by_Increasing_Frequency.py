# 時間複雜度:O(nlog(n))
# 空間複雜度: O(n)
class Solution:
    def frequencySort(self, nums):
        count = {}
        
        # count = collections.Counter(nums)
        for i in nums:
            count[i] = count.get(i, 0) + 1
            
        nums.sort(key=lambda x: [count[x], -x])
        return nums

p = Solution()
print(p.frequencySort([1, 1, 2, 2, 2, 3]))