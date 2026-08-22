# LeetCode 3116
# Kth Smallest Amount With Single Denomination Combination

class Solution:

    # Find GCD (Greatest Common Divisor)
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Find LCM (Least Common Multiple)
    def lcm(self, a, b):
        return (a // self.gcd(a, b)) * b

    # Count how many valid amounts are <= x
    def count(self, coins, x):

        n = len(coins)
        total = 0

        # Try every possible combination of coins
        # Example for 3 coins:
        # 001 -> coin 1
        # 010 -> coin 2
        # 011 -> coin 1 + coin 2
        # etc.

        for mask in range(1, 1 << n):

            current_lcm = 1
            number_of_coins = 0

            for i in range(n):

                # Check whether coin i is selected
                if mask & (1 << i):

                    number_of_coins += 1

                    current_lcm = self.lcm(
                        current_lcm,
                        coins[i]
                    )

                    # If LCM is already bigger than x,
                    # it cannot contribute any number <= x.
                    if current_lcm > x:
                        break

            # If current LCM is bigger than x,
            # there are zero multiples <= x.
            if current_lcm > x:
                continue

            # Number of multiples of current_lcm <= x
            amount = x // current_lcm

            # Inclusion-Exclusion:
            # Odd number of selected coins -> ADD
            # Even number of selected coins -> SUBTRACT

            if number_of_coins % 2 == 1:
                total += amount
            else:
                total -= amount

        return total

    def findKthSmallest(self, coins, k):

        # The answer cannot be bigger than:
        # smallest coin * k
        left = 1
        right = min(coins) * k

        # Binary Search
        while left < right:

            mid = (left + right) // 2

            # How many valid amounts are <= mid?
            count = self.count(coins, mid)

            if count >= k:
                # Answer could be mid or smaller
                right = mid

            else:
                # We need a bigger number
                left = mid + 1

        return left


# --------------------------------------------------
# TESTING IN VS CODE
# --------------------------------------------------

if __name__ == "__main__":

    solution = Solution()

    # Example 1
    coins = [3, 6, 9]
    k = 3

    answer = solution.findKthSmallest(coins, k)

    print("Example 1")
    print("Coins:", coins)
    print("K:", k)
    print("Answer:", answer)

    print()

    # Example 2
    coins = [5, 2]
    k = 7

    answer = solution.findKthSmallest(coins, k)

    print("Example 2")
    print("Coins:", coins)
    print("K:", k)
    print("Answer:", answer)