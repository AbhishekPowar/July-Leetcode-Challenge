class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(s, cur):
            if s:
                for word in self.words:
                    if s == word:
                        self.ans.append(' '.join(cur+[word]))
                    elif s.startswith(word):
                        dfs(s[len(word):], cur+[word])

        self.words = set(wordDict)
        self.ans = []
        # checking whether letters in s are in dict
        if set(''.join(self.words)) & set(s) == set(s):
            dfs(s, [])
        return self.ans

#
