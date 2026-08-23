"""
LeetCode 1927 - Sum Game
Difficulty: Medium
Approach: Mathematical / Greedy
Time Complexity: O(n)
Space Complexity: O(1)
"""


def sumGame(num):
    n = len(num)
    half = n // 2

    left_sum = 0
    right_sum = 0

    left_questions = 0
    right_questions = 0

    # Process the first half
    for i in range(half):
        if num[i] == '?':
            left_questions += 1
        else:
            left_sum += int(num[i])

    # Process the second half
    for i in range(half, n):
        if num[i] == '?':
            right_questions += 1
        else:
            right_sum += int(num[i])

    # Bob can force the two sums to be equal
    if 2 * (left_sum - right_sum) == 9 * (right_questions - left_questions):
        return False

    # Otherwise, Alice can force the sums to be different
    return True


# Take input from the user
num = input("Enter num: ").strip()

# Call the function
result = sumGame(num)

# Display the result
print("Alice wins:", result)