# reverse words in a string and remove all the trailing,leading and unwanted white spaces
class Solution(object):
    def reverseWords(self, s):
        
        news=s.split(' ')
        news.reverse()
        res=' '.join(news).strip(' ')
        return ' '.join(res.split())
        
s='   hello    world ' 
obj=Solution()
print(obj.reverseWords(s))
    
        
