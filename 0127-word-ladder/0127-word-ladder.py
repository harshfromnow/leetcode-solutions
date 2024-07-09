class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList=set(wordList)
        if endWord not in wordList:
            return 0
        char=set()
        for k in wordList:
            for j in k:
                char.add(j)
        queue=deque([(beginWord,1)])
        while queue:
            current,trans=queue.popleft()
            if current==endWord:
                return trans
            for i in range(len(current)):
                for c in char:
                    if c!=current[i]:
                        new=current[:i]+c+current[i+1:]
                        if new in wordList:
                            queue.append([new,trans+1])
                            wordList.remove(new)
        return 0
        