# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def containsDuplicate(self, nums):
        count = {}
        for i in nums:
            if i in count:
                return True
            else:
                count[i] = 1
            
        return False
p = Solution()
print(p.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))


# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

p = Solution()
print(p.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
        

class Solution:
    def containsDuplicate(self, nums):
        hashSet = set()

        for i in nums:
            if i in hashSet:
                return True
            else:
                hashSet.add(i)
                
        return False
    
p = Solution()
print(p.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
