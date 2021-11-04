# 時間複雜度: O(1)
# 時間複雜度: O(1)
class Solution:
    def reformatDate(self, date):     
        Month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        date = date.split(' ')[::-1]
        date[1] = f'{Month.index(date[1]) + 1:0>2}'
        date[2] = f'{date[2][0:len(date[2])-2]:0>2}'
           
        return '-'.join(date)

p = Solution()
print(p.reformatDate("20th Oct 2052"))