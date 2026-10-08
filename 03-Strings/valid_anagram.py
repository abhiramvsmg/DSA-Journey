class Solution:
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            count[char] = count.get(char, 0) - 1

        for value in count.values():
            if value != 0:
                return False

        return True


solution = Solution()

print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("rat", "car"))