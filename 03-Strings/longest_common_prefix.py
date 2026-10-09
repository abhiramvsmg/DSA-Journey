class Solution:
    def longestCommonPrefix(self, strs):
        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix
solution = Solution()

print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))
print(solution.longestCommonPrefix(["interspecies", "interstellar", "interstate"]))