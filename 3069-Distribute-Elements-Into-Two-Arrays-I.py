"""
LeetCode 3069 - Distribute Elements Into Two Arrays I
Difficulty: Easy
Approach: Simulation
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution(object):
    def resultArray(self, nums):
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2


# -----------------------------
# Main Program
# -----------------------------

nums = list(map(int, input("Enter the no. separated by space :").split()))

solution = Solution()

result = solution.resultArray(nums)

print("Input:", nums)
print("Output:", result)