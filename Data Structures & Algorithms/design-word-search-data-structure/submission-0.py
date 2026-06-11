class TrieNode:
    def __init__(self):

        # Dictionary mapping characters to child nodes.
        self.children = {}

        # True if a complete word ends at this node.
        self.word = False


class WordDictionary:

    def __init__(self):

        # Root of the Trie.
        self.root = TrieNode()

    def addWord(self, word: str) -> None:

        # Start at the root node.
        cur = self.root

        # Insert each character into the Trie.
        for c in word:

            # Create a new node if necessary.
            if c not in cur.children:
                cur.children[c] = TrieNode()

            # Move to the next node.
            cur = cur.children[c]

        # Mark the end of the word.
        cur.word = True

    def search(self, word: str) -> bool:

        def dfs(j, root):

            # Start searching from the given node.
            cur = root

            # Process characters from position j onward.
            for i in range(j, len(word)):
                c = word[i]

                # Wildcard case: '.' can match any character.
                if c == ".":

                    # Try every possible child.
                    for child in cur.children.values():

                        # If any path succeeds, return True.
                        if dfs(i + 1, child):
                            return True

                    # No child produced a match.
                    return False

                # Normal character case.
                else:

                    # Character doesn't exist.
                    if c not in cur.children:
                        return False

                    # Move to the matching child node.
                    cur = cur.children[c]

            # We've consumed the entire word.
            # Return True only if a word ends here.
            return cur.word

        # Start DFS from the root.
        return dfs(0, self.root)