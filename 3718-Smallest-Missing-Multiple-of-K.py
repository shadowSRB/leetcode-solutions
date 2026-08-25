"""
LeetCode 3718 - Smallest Missing Multiple of K
Difficulty: Easy
Approach: Hash Set
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution(object):
    def missingMultiple(self, nums, k):
        # Convert list to set for fast searching
        nums_set = set(nums)

        # Start with the first positive multiple of k
        multiple = k

        # Keep checking multiples of k
        while multiple in nums_set:
            multiple += k

        # Return the first missing multiple
        return multiple


# --------------------------------
# Test the solution
# --------------------------------

solution = Solution()

# Example 1
nums = [8, 2, 3, 4, 6]
k = 2

answer = solution.missingMultiple(nums, k)
print("Example 1:", answer)


# Example 2
nums = [1, 4, 7, 10, 15]
k = 5

answer = solution.missingMultiple(nums, k)
print("Example 2:", answer)


# Example 3
nums = [2, 4, 6, 8]
k = 2

answer = solution.missingMultiple(nums, k)
print("Example 3:", answer)