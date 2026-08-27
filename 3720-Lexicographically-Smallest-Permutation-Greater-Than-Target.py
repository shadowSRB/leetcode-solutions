class Solution(object):
    def lexGreaterPermutation(self, s, target):
        n = len(s)

        # Count characters in s
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Try changing target from right to left
        for i in range(n - 1, -1, -1):

            # Count characters needed for target[:i]
            prefix_count = [0] * 26

            for j in range(i):
                prefix_count[ord(target[j]) - ord('a')] += 1

            # Check if target[:i] can be made from s
            possible = True

            for j in range(26):
                if prefix_count[j] > count[j]:
                    possible = False
                    break

            if not possible:
                continue

            # Characters left after using target[:i]
            remaining = count[:]

            for j in range(26):
                remaining[j] -= prefix_count[j]

            # Find smallest character greater than target[i]
            target_char = ord(target[i]) - ord('a')

            for j in range(target_char + 1, 26):

                if remaining[j] > 0:

                    # Use this character
                    remaining[j] -= 1

                    # Put remaining characters in sorted order
                    suffix = []

                    for k in range(26):
                        suffix.append(chr(k + ord('a')) * remaining[k])

                    return target[:i] + chr(j + ord('a')) + ''.join(suffix)

        return ""


# -----------------------------------
# Test the solution
# -----------------------------------

solution = Solution()

# Test Case 1
s = "abc"
target = "bba"

answer = solution.lexGreaterPermutation(s, target)

print("Input:")
print("s =", s)
print("target =", target)
print("Output:", answer)


# Test Case 2
s = "leet"
target = "code"

answer = solution.lexGreaterPermutation(s, target)

print("\nInput:")
print("s =", s)
print("target =", target)
print("Output:", answer)


# Test Case 3
s = "baba"
target = "bbaa"

answer = solution.lexGreaterPermutation(s, target)

print("\nInput:")
print("s =", s)
print("target =", target)
print("Output:", answer)