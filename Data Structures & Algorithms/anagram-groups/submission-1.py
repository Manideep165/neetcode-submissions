class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         # defaultdict(list)
        # Automatically creates an empty list if the key
        # does not already exist.
        #
        # Example:
        # res["abc"] -> []
        #
        # This lets us append directly without checking
        # if the key already exists.
        
        res = defaultdict(list)

        for s in strs: # Loop through every string in the input list
            # Create a frequency array of size 26
            # representing letters a-z.
            #
            # Initially all counts are 0.
            #
            # Example:
            # [0,0,0,0,0,0,...]
            count = [0] * 26

            for c in s: # Loop through every character in the string

                # ord(c) gives ASCII value of character
                #
                # ord("a") = 97
                # ord("b") = 98
                #
                # By subtracting ord("a"),
                # we map letters to indices:
                #
                # a -> 0
                # b -> 1
                # c -> 2
                #
                # Example:
                # c = "t"
                #
                # ord("t") - ord("a")
                # 116 - 97
                # = 19
                #
                # So index 19 represents letter 't'
                count[ord(c) - ord("a")] += 1
            
            # Lists cannot be dictionary keys because
            # they are mutable.
            #
            # So we convert the list into a tuple.
            #
            # Example:
            # [1,0,0,1] -> (1,0,0,1)
            #
            # All anagrams will generate the SAME tuple.
            #
            # Example:
            # "eat", "tea", "ate"
            # all produce identical frequency counts.
            #
            # We use that tuple as the dictionary key.

            res[tuple(count)].append(s)

             # append(s)
            # adds the current string into the group
            # corresponding to that frequency pattern.

        # res.values() returns all grouped lists
        #
        # Example:
        # dict_values([["eat","tea","ate"], ["tan","nat"]])
        #
        # Convert it into a normal list before returning.

        return list(res.values())      