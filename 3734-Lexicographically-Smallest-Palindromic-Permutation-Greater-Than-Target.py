"""
LeetCode 3734 - Lexicographically Smallest Palindromic Permutation Greater Than Target
Difficulty: Hard
Approach: Frequency Count + Greedy
Time Complexity: O(n^2)
Space Complexity: O(n)
"""
class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        n = len(s)

        # Count characters in s
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Check whether a palindrome is possible
        odd = 0
        middle = ""

        for i in range(26):
            if count[i] % 2 == 1:
                odd += 1
                middle = chr(i + ord('a'))

        if odd > 1:
            return ""

        # Characters available for the left half
        half = [x // 2 for x in count]
        half_len = n // 2

        # Build the complete palindrome
        def build(left):
            if n % 2 == 1:
                return left + middle + left[::-1]
            else:
                return left + left[::-1]

        # -------------------------------------------------
        # First, try target's first half exactly
        # -------------------------------------------------
        remaining = half[:]
        possible = True

        for i in range(half_len):
            idx = ord(target[i]) - ord('a')

            if remaining[idx] == 0:
                possible = False
                break

            remaining[idx] -= 1

        if possible:
            left = target[:half_len]
            candidate = build(left)

            if candidate > target:
                return candidate

        # -------------------------------------------------
        # Find the smallest left half greater than target
        # -------------------------------------------------
        for i in range(half_len - 1, -1, -1):

            remaining = half[:]
            possible = True

            # Keep target[:i] the same
            for j in range(i):
                idx = ord(target[j]) - ord('a')

                if remaining[idx] == 0:
                    possible = False
                    break

                remaining[idx] -= 1

            if not possible:
                continue

            # Find the smallest character greater than target[i]
            target_idx = ord(target[i]) - ord('a')
            chosen = -1

            for c in range(target_idx + 1, 26):
                if remaining[c] > 0:
                    chosen = c
                    break

            if chosen == -1:
                continue

            # Add the chosen character
            left = target[:i]
            left += chr(chosen + ord('a'))

            remaining[chosen] -= 1

            # Add remaining characters in sorted order
            for c in range(26):
                left += chr(c + ord('a')) * remaining[c]

            # Build the palindrome
            candidate = build(left)

            if candidate > target:
                return candidate

        return ""


# =====================================================
# PRACTICE / TESTING
# =====================================================

solution = Solution()

# Example 1
s = "baba"
target = "abba"

answer = solution.lexPalindromicPermutation(s, target)

print("Example 1")
print("s      =", s)
print("target =", target)
print("answer =", answer)


# Example 2
s = "baba"
target = "bbaa"

answer = solution.lexPalindromicPermutation(s, target)

print("\nExample 2")
print("s      =", s)
print("target =", target)
print("answer =", answer)


# Example 3
s = "abc"
target = "abb"

answer = solution.lexPalindromicPermutation(s, target)

print("\nExample 3")
print("s      =", s)
print("target =", target)
print("answer =", answer)


# Example 4
s = "aac"
target = "abb"

answer = solution.lexPalindromicPermutation(s, target)

print("\nExample 4")
print("s      =", s)
print("target =", target)
print("answer =", answer)


# =====================================================
# TRY YOUR OWN TEST
# =====================================================

s = input("\nEnter s: ")
target = input("Enter target: ")

answer = solution.lexPalindromicPermutation(s, target)

print("Answer:", answer)