class Solution:

    def isValid(self, s: str) -> bool:

        # Stack stores opening brackets
        #
        # Example:
        # "("
        # "{"
        # "["
        stack = []

        # Dictionary maps:
        #
        # closing bracket -> matching opening bracket
        #
        # Example:
        # ")" -> "("
        ClosetoOpen = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        # Traverse every character
        for c in s:

            # If current character is
            # a closing bracket
            if c in ClosetoOpen:

                # Check:
                #
                # 1. stack is NOT empty
                # 2. top of stack matches
                #    required opening bracket
                #
                # stack[-1] = top element
                if stack and stack[-1] == ClosetoOpen[c]:

                    # Matching pair found
                    #
                    # Remove opening bracket
                    stack.pop()

                else:

                    # Invalid case:
                    #
                    # Example:
                    # "]"
                    # "(]"
                    #
                    # No matching opening bracket
                    return False

            else:

                # Current character is
                # an opening bracket
                #
                # Push into stack
                stack.append(c)

        # Valid only if stack becomes empty
        #
        # Empty stack means:
        # all brackets matched correctly
        return True if not stack else False