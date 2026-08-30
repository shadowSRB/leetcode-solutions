"""
LeetCode 2091 - Removing Minimum and Maximum From Array
Difficulty: Medium
Approach: Index Calculation / Greedy
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)

        # Find the positions of minimum and maximum
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        # Make sure left is the smaller index
        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # Option 1: Remove both from the left
        option1 = right + 1

        # Option 2: Remove both from the right
        option2 = n - left

        # Option 3: Remove one from left and one from right
        option3 = left + 1 + n - right

        # Return the minimum number of deletions
        return min(option1, option2, option3)


# -------------------------------
# Test the solution
# -------------------------------

nums = [2, 10, 7, 5, 4, 1, 8, 6]

solution = Solution()

answer = solution.minimumDeletions(nums)

print("Array:", nums)
print("Minimum deletions:", answer)