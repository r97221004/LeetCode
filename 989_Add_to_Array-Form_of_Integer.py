# 時間複雜度:  O(max(n, log k))
class Solution:
    def addToArrayForm(self, num, k):
        for i in range(len(num) - 1, -1, -1):
            num[i] += k
            if num[i] < 10:
                return num
            k, num[i] = divmod(num[i], 10)    # k, num[i] = num[i]//10, num[i]%10
        
        while k >= 10:
            k, m = divmod(k, 10)
            num = [m] + num
            
        return [k] + num

p = Solution()
print(p.addToArrayForm([2,1,5], 806))