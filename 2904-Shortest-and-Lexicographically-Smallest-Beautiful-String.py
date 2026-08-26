class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        n = len(s)
        ans = ""

        for i in range(n):
            ones = 0

            for j in range(i, n):
                if s[j] == '1':
                    ones += 1

                if ones == k:
                    current = s[i:j + 1]

                    if (ans == "" or
                        len(current) < len(ans) or
                        (len(current) == len(ans) and current < ans)):
                        ans = current

                    break

        return ans


# -------------------------------
# Test the solution
# -------------------------------

solution = Solution()

# Example 1
s = "100011001"
k = 3
print("Example 1:", solution.shortestBeautifulSubstring(s, k))

# Example 2
s = "1011"
k = 2
print("Example 2:", solution.shortestBeautifulSubstring(s, k))

# Example 3
s = "000"
k = 1
print("Example 3:", solution.shortestBeautifulSubstring(s, k))