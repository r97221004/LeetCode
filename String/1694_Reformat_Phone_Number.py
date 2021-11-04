# 時間複雜度: O(n)
# 空間複雜度: O(n)
class Solution:
    def reformatNumber(self, number):
        number = number.replace("-", "").replace(" ", "")  
        ans = []
        
        for i in range(0, len(number), 3): 
            if len(number) - i != 4: ans.append(number[i:i+3])  # 切片可以超出範圍，索引不行。
            else: 
                ans.extend([number[i:i+2], number[i+2:]])
                break 

        return "-".join(ans)

p = Solution()
print(p.reformatNumber("123 4-567"))