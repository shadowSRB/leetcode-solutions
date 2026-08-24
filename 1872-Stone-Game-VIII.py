"""
LeetCode 1872 - Stone Game VIII
Difficulty: Hard
Approach: Prefix Sum + Dynamic Programming
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution(object):
    def stoneGameVIII(self, stones):
        prefix = []
        total = 0

        for stone in stones:
            total += stone
            prefix.append(total)

        ans = prefix[-1]

        for i in range(len(stones) - 2, 0, -1):
            ans = max(ans, prefix[i] - ans)

        return ans


# -----------------------------
# Test the solution
# -----------------------------

solution = Solution()

# Example 1
stones = [-1, 2, -3, 4, -5]
print("Example 1:", solution.stoneGameVIII(stones))

# Example 2
stones = [7, -6, 5, 10, 5, -2, -6]
print("Example 2:", solution.stoneGameVIII(stones))

# Example 3
stones = [-10, -12]
print("Example 3:", solution.stoneGameVIII(stones))