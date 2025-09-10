class Solution:
    def simplifyPath(self, path: str) -> str:
        
        chain = []
        for p in path.split('/'):
            if not p:
                continue
            elif p == '.':
                continue
            elif p == '..':
                if chain:
                    chain.pop()
                continue
            else:
                chain.append(p)
        
        return '/' + '/'.join(chain)