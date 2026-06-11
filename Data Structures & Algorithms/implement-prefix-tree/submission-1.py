class TrieNode:
    def __init__(self):
        # Stores child nodes for each character.
        self.children = {}

        # True if a complete word ends at this node.
        self.endOfWord = False


class PrefixTree:

    def __init__(self):
        # Create the root node of the Trie.
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        # Start at the root.
        cur = self.root

        # Process each character in the word.
        for c in word:

            # Create a new node if necessary.
            if c not in cur.children:
                cur.children[c] = TrieNode()

            # Move to the next node.
            cur = cur.children[c]

        # Mark the end of the word.
        cur.endOfWord = True

    def search(self, word: str) -> bool:

        # Start at the root.
        cur = self.root

        # Traverse the Trie.
        for c in word:

            # Word doesn't exist if a character is missing.
            if c not in cur.children:
                return False

            cur = cur.children[c]

        # Return True only if this is a complete word.
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:

        # Start at the root.
        cur = self.root

        # Traverse the prefix.
        for c in prefix:

            # Prefix doesn't exist.
            if c not in cur.children:
                return False

            cur = cur.children[c]

        # Entire prefix was found.
        return True