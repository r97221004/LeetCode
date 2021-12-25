# 時間複雜度: O(n)
# 空間複雜度: O(1)
class Solution:
    def sumOddLengthSubarrays(self, arr):
        res = 0
        freq = 0
        n = len(arr)
        
        for i in range(n):
            freq = freq - (i + 1)//2 + (n - i + 1)//2
            res += freq*arr[i]
        
        return res
    
p = Solution()
print(p.sumOddLengthSubarrays([1, 4, 2, 5, 3]))


# 時間複雜度: O(n*n) ?
# 空間複雜度: O(n)
class Solution:
    def sumOddLengthSubarrays(self, arr):
        res = 0
        
        for i in range(len(arr)):
            end = i + 1
            while end <= len(arr):
                res += sum(arr[i: end])
                end += 2
                
        return res 
    
p = Solution()
print(p.sumOddLengthSubarrays([1, 4, 2, 5, 3]))