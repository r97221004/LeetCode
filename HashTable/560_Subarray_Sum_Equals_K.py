# 時間複雜度: O(n*n)
# 空間複雜度: O(1)
# 這題用這個方法會 Time Limit Exceeded(TLE)
class Solution:
    def subarraySum(self, nums, k):
        res = 0
        carry = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                carry += nums[j]
                if carry == k:
                    res += 1
            else:
                carry = 0
                    
        return res

p = Solution()
print(p.subarraySum([1, -1, 0], 0))


# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def subarraySum(self, nums, k):
        count = 0
        sums = 0
        d = {}
        d[0] = 1
        
        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums - k, 0)
            d[sums] = d.get(sums, 0) + 1
            
        return count

p = Solution()
print(p.subarraySum([1, -1, 0], 0))