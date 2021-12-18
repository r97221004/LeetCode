# 時間複雜度: O(n)
# 空間複雜度: O(1), result 不計入
class Solution:
    def fizzBuzz(self, n):
        res = []
        
        for i in range(1, n + 1):
            if i%3 == 0 and i%5 == 0:
                res.append("FizzBuzz")
            elif i%3 ==0:
                res.append("Fizz")
            elif i%5 ==0:
                res.append("Buzz")
            else:
                res.append(str(i))
                
        return res
            
p = Solution()
print(p.fizzBuzz(15))