class Solution:

    def encode(self, strs: List[str]) -> str:
        # Final encoded string
        res = ""
        for s in strs: # Loop through each string
            res += str(len(s)) + "#" + s

            # Store:
            # length + '#' + actual string
            #
            # Example:
            # "neet" -> "4#neet"
        return res

    def decode(self, s: str) -> List[str]:
        # Result list, Pointer to traverse encoded string
        res, i = [], 0

        # Continue until end of string
        while i < len(s):
            # j will find the '#'
            j = i
            # Move j until '#'
            while s[j] != "#":
                j += 1

            # Characters before '#' represent length
            #
            # Example:
            # "4#neet"
            #
            # s[i:j] = "4"
            length = int(s[i:j])

            # Extract actual word
            #
            # Start:
            # j + 1
            #
            # End:
            # j + 1 + length
            #
            # Example:
            # "4#neet"
            #
            # start = 2
            # end = 6
            #
            # gives:
            # "neet"
            res.append(s[j + 1 : j + 1 + length])

            # Move i to next encoded word
            #
            # Skip:
            # length digits
            # '#'
            # actual word
            i = j + 1 + length
        return res
