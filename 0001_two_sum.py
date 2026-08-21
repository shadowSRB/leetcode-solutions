""" 
 LeetCode 1 - Two Sum
 Difficulty: Easy
 Approach: Hash Map
 Time Complexity: O(n)
 Space Complexity: O(n) 
"""

def twoSum(nums, target):
    seen = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in seen:
            return [seen[complement], i]

        seen[nums[i]] = i


# Take input from the user
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter target: "))

# Call the function
result = twoSum(nums, target)

# Display the answer
print("Indices:", result)
