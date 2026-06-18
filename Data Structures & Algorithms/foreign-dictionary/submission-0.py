class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # Build adjacency list:
        # character -> set of characters that must come after it.
        adj = {c: set() for w in words for c in w}

        # Compare adjacent words to determine ordering rules.
        for i in range(len(words) - 1):

            w1, w2 = words[i], words[i + 1]

            # Compare only up to the shorter length.
            minLen = min(len(w1), len(w2))

            # Invalid case:
            # ["abc", "ab"]
            #
            # A longer word appears before its prefix.
            if (
                len(w1) > len(w2) and
                w1[:minLen] == w2[:minLen]
            ):
                return ""

            # Find the first differing character.
            for j in range(minLen):

                if w1[j] != w2[j]:

                    # Character in w1 must come before
                    # character in w2.
                    adj[w1[j]].add(w2[j])

                    # Only the first difference matters.
                    break

        # Tracks DFS state:
        # True  = currently visiting
        # False = fully processed
        visit = {}

        # Stores topological ordering.
        res = []

        def dfs(c):

            # Node already visited.
            if c in visit:
                return visit[c]

            # Mark as currently visiting.
            visit[c] = True

            # Visit all neighbors.
            for nei in adj[c]:

                # Cycle detected.
                if dfs(nei):
                    return True

            # Mark as fully processed.
            visit[c] = False

            # Add to topological order.
            res.append(c)

        # Run DFS from every character.
        for c in adj:

            if dfs(c):
                return ""

        # Reverse postorder gives topological sort.
        res.reverse()

        return "".join(res)