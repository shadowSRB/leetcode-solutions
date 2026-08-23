"""
LeetCode 3471 - Find the Largest Almost Missing Integer
Difficulty: Easy
Approach: Sliding Window + Hash Map
Time Complexity: O(n * k)
Space Complexity: O(k)
"""

def largestInteger(nums, k):

    # Dictionary to store how many subarrays
    # contain each number
    count = {}

    # Find all subarrays of size k
    for i in range(len(nums) - k + 1):

        # Get current subarray
        # set() makes sure we count a number
        # only once inside the same subarray
        window = set(nums[i:i + k])
        print(f"Subarray of size {k} starting at index {i}: {window}")

      
        # Count each number in this subarray
        for x in window:
            count[x] = count.get(x, 0) + 1

    # Start with -1
    ans = -1

    # Find numbers that appear in exactly one subarray
    for x in count:

        if count[x] == 1:

            # Keep the largest number
            ans = max(ans, x)
            print(f"Number {x} appears in exactly one subarray of size {k}.")

    return ans

# Take input from user
nums = list(map(int, input("Enter the numbers: ").split()))

# Take k from user
k = int(input("Enter k: "))

# Call the function
result = largestInteger(nums, k)

# Display the answer
print("Largest almost missing integer:", result)