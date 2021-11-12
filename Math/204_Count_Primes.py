# 時間複雜度: O(n*n)
# 空間複雜度: O(1)
class Solution:
    def countPrimes(self, n):
        res = 0
        for i in range(2, n):
            for j in range(2, i - 1):
                if i%j == 0:
                    break
            
            else:
                res += 1
                
        return res

p = Solution()
print(p.countPrimes(10))
                

# 時間複雜度: O(sqrt(n)*log(log(n)))
# 空間複雜度: O(n)
# Sieve of Eratosthenes
class Solution:
    def countPrimes(self, n):
        if n < 2:
            return 0
        
        res = [1]*(n)
        res[0] = res[1] = 0
        
        for i in range(2, int(n**0.5) + 1):
            if res[i] == 1:
                res[i*i:n:i] = [0]*len(res[i*i:n:i])
                
        return sum(res)

p = Solution()
print(p.countPrimes(10))