class Solution:
    def get_all_indices(self, s, token):
        token_len = len(token)
        result = []
        for i in range(len(s) - token_len + 1):
            if s[i: i + token_len] == token:
                result.append(i)
        return result
    
    def addBoldTag(self, s: str, words: List[str]) -> str:
        hash_set = set()
        for token in words:
            indices = self.get_all_indices(s, token)
            for item in indices:
                for i in range(item, item + len(token)):
                    hash_set.add(i)
        print(hash_set)
        idx = 0
        token = []
        while idx < len(s):
            if idx in hash_set:
                token.append("<b>")
                token.append(s[idx])
                idx += 1
                while idx in hash_set:
                    token.append(s[idx])
                    idx += 1
                token.append("</b>")
            else:
                token.append(s[idx])
                idx += 1
        return ''.join(token)
            
        
        
            
        
        
        
        