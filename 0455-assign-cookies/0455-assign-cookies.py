class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        result, i, j = 0, 0, 0
        while j < len(s) and i < len(g):
            if g[i] <= s[j]:
                result += 1
                i += 1
                j += 1
            else:
                j += 1
        return result
        