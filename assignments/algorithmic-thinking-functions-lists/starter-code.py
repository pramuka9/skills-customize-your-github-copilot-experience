"""Starter code for: Algorithmic Thinking with Functions and Lists"""

# Task 1

def count_evens(numbers):
    # Return how many values in numbers are even.
    pass


def find_maximum(numbers):
    # Return the largest number without using max().
    # Return None if numbers is empty.
    pass


def analyze_numbers(numbers):
    # Return a dictionary with:
    # count, even_count, maximum, average
    # For an empty list, maximum and average should be None.
    pass


# Task 2

def is_sorted(numbers):
    # Return True if numbers is in non-decreasing order.
    pass


def is_almost_sorted(numbers):
    # Return True if numbers is already sorted, or can be sorted
    # by swapping exactly one pair of elements.
    pass


def run_tests():
    # Add at least 5 test cases for is_almost_sorted.
    test_cases = [
        ([1, 2, 3, 4], True),
        ([1, 3, 2, 4], True),
        ([3, 1, 2, 4], False),
        ([], True),
        ([5], True),
    ]

    for numbers, expected in test_cases:
        actual = is_almost_sorted(numbers)
        print(f"numbers={numbers} expected={expected} actual={actual}")


if __name__ == "__main__":
    sample = [3, 8, 1, 10, 5, 6]
    print("Analyze sample:", analyze_numbers(sample))
    run_tests()
