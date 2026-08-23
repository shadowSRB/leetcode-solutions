"""
LeetCode 1386 - Cinema Seat Allocation
Difficulty: Medium
Approach: Hash Map + Set
Time Complexity: O(n)
Space Complexity: O(n)
"""
def maxNumberOfFamilies(n, reservedSeats):

    # Store reserved seats row by row
    rows = {}

    for row, seat in reservedSeats:
        if row not in rows:
            rows[row] = set()

        rows[row].add(seat)

    # Start with 2 groups for every row
    answer = (n - len(rows)) * 2

    # Check rows that have reserved seats
    for row in rows:

        seats = rows[row]

        left = True
        right = True
        middle = True

        # Check seats 2,3,4,5
        for seat in [2, 3, 4, 5]:
            if seat in seats:
                left = False

        # Check seats 6,7,8,9
        for seat in [6, 7, 8, 9]:
            if seat in seats:
                right = False

        # Check seats 4,5,6,7
        for seat in [4, 5, 6, 7]:
            if seat in seats:
                middle = False

        # If left and right are available
        if left and right:
            answer += 2

        # If only one of left/right is available
        elif left or right:
            answer += 1

        # If neither left nor right works,
        # try the middle
        elif middle:
            answer += 1

    return answer


# -----------------------------
# Taking input from user
# -----------------------------

n = int(input("Enter number of rows: "))

number = int(input("Enter number of reserved seats: "))

reservedSeats = []

for i in range(number):
    row, seat = map(
        int,
        input("Enter row and seat: ").split()
    )

    reservedSeats.append([row, seat])


# Call the function
result = maxNumberOfFamilies(n, reservedSeats)

# Print answer
print("Maximum number of families:", result)