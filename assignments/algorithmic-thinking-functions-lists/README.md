# 📘 Assignment: Algorithmic Thinking with Functions and Lists

## 🎯 Objective

Practice algorithmic problem solving by breaking down challenges into steps, writing reusable helper functions, and processing lists in Python.

## 📝 Tasks

### 🛠️	Build a Number Analyzer

#### Description
Write functions that analyze a list of integers and return useful summary results. Use helper functions to keep your logic clear and reusable.

#### Requirements
Completed program should:

- Implement `count_evens(numbers)` to return how many even numbers are in the list
- Implement `find_maximum(numbers)` without using Python's built-in `max()`
- Implement `analyze_numbers(numbers)` that returns a dictionary with keys `count`, `even_count`, `maximum`, and `average`
- Handle an empty list safely by returning `None` for `maximum` and `average`


### 🛠️	Solve a Step-by-Step Challenge

#### Description
Create an algorithm that checks whether a sequence of numbers is "almost sorted". A sequence is almost sorted if it is already sorted in non-decreasing order, or can become sorted by swapping exactly one pair of elements.

#### Requirements
Completed program should:

- Implement `is_sorted(numbers)` to verify non-decreasing order
- Implement `is_almost_sorted(numbers)` using clear step-by-step logic
- Return `True` if the list is sorted or one swap away from sorted; otherwise return `False`
- Include at least 5 test cases that cover normal and edge cases
