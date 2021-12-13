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
        data = {}
        data[0] = 1
        
        for i in nums:
            sums += i
            count += data.get(sums - k, 0)
            data[sums] = data.get(sums, 0) + 1
        
        return count

p = Solution()
print(p.subarraySum([1, -1, 0], 0))

# First of all, the basic idea behind this code is that, whenever the sums has increased by a value of k, we've found a subarray of sums=k.
# I'll also explain why we need to initialise a 0 in the hashmap.
# Example: Let's say our elements are [1,2,1,3] and k = 3.
# and our corresponding running sums = [1,3,4,7]
# Now, if you notice the running sums array, from 1->4, there is increase of k and from 4->7, there is an increase of k. So, we've found 2 subarrays of sums=k.

# But, if you look at the original array, there are 3 subarrays of sums==k. Now, you'll understand why 0 comes in the picture.

# In the above example, 4-1=k and 7-4=k. Hence, we concluded that there are 2 subarrays.
# However, if sums==k, it should've been 3-0=k. But 0 is not present in the array. To account for this case, we include the 0.
# Now the modified sums array will look like [0,1,3,4,7]. Now, try to see for the increase of k.

# 0->3
# 1->4
# 4->7
# Hence, 3 sub arrays of sums=k