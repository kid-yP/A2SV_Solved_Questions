class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['#'] = word

        m, n = len(board), len(board[0])
        result = set()

        def dfs(i: int, j: int, node: dict):
            ch = board[i][j]
            if ch not in node:
                return
            node = node[ch]

            if '#' in node:
                result.add(node['#'])

            board[i][j] = '#'

            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                    dfs(ni, nj, node)

            board[i][j] = ch

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)

        return list(result)