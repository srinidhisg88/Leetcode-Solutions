class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q=deque([])
        hashset=set([w for w in wordList])
        q.append((beginWord,1))
        
        if beginWord in wordList:

            hashset.remove(beginWord)
        while q:
            word,cnt=q.popleft()
            if word==endWord:
                return cnt
            for i in range(len(word)):
                wordarr=list(word)
                original_char=wordarr[i]
                for char in string.ascii_lowercase:
                    
                    wordarr[i]=char
                    replacedword=''.join(wordarr)
                    if replacedword in hashset:
                        hashset.remove(replacedword)
                        q.append((replacedword,cnt+1))
                wordarr[i]=original_char
        return 0    
