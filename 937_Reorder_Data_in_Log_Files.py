# Let N be the number of logs in the list and M be the maximum length of a single log.
# 時間複雜度: O(M*N*log(N))
# 空間複雜度: O(N*M)
class Solution:
    def reorderLogFiles(self, logs):
        digits = []
        letters = []
		
        for i in logs:
            if i.split(' ')[1].isdigit():
                digits.append(i)
            else:
                letters.append(i)
        
        letters.sort(key = lambda x:x.split(' ')[0])
        letters.sort(key = lambda x:x.split(' ')[1:])
        result = letters + digits
        return result

p = Solution()
print(p.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))

