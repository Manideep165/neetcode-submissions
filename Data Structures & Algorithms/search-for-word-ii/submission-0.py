class TrieNode:
    def __init__(self):

        # Maps characters to child Trie nodes.
        self.children = {}

        # True if a complete word ends here.
        self.isWord = False

    def addWord(self, word):

        # Start from current node (usually root).
        cur = self

        for c in word:

            # Create child node if necessary.
            if c not in cur.children:
                cur.children[c] = TrieNode()

            # Move to next node.
            cur = cur.children[c]

        # Mark the end of the word.
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Build Trie containing all target words.
        root = TrieNode()

        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])

        # Stores found words.
        res = set()

        # Tracks cells currently in DFS path.
        visit = set()

        def dfs(r, c, node, word):

            # Stop if:
            # 1. Out of bounds
            # 2. Cell already used
            # 3. Character not in Trie path
            if (
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r, c) in visit or
                board[r][c] not in node.children
            ):
                return

            # Mark current cell as visited.
            visit.add((r, c))

            # Move to next Trie node.
            node = node.children[board[r][c]]

            # Extend current word.
            word += board[r][c]

            # Found a complete word.
            if node.isWord:
                res.add(word)

            # Explore all 4 directions.
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            # Backtrack.
            visit.remove((r, c))

        # Start DFS from every cell.
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)