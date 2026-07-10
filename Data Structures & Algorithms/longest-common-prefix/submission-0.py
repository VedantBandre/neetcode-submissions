class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        sortedStrings = sorted(strs)
        firstString, lastString = sortedStrings[0], sortedStrings[-1]

        for index, character in enumerate(firstString):
        # if we reached end of first string or the characters do not match
            if (index > len(lastString)) or character != lastString[index]:
                # return firstString only uptil that index(that satisfies the 'if')
                return firstString[:index]

        return firstString