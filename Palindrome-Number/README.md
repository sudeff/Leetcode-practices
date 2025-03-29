Palindrome Number

Problem Description:
Given an integer `x`, return `True` if `x` is a palindrome, and `False` otherwise.

An integer is a palindrome when it reads the same backward as forward.  
> For example: `121` is a palindrome, but `123` is not.

Constraints
- `-2^31 <= x <= 2^31 - 1`
- Negative numbers are not considered palindromes.

Approach:
  Bottom-Up Dynamic Programming 
  The solution uses a Fibonacci-like recurrence where the number of ways to reach step `n` is the sum of the ways to reach steps `n-1` and `n-2`.  
  Instead of storing all values in a list, we use two variables (`a`, `b`) to store the last two computed values and update them in a loop — effectively using **O(1) space**.
Time & Space Complexity

Time Complexity : O(n)
Space Complexity: O(1)

n is the number of digits in `x`.

Python Code:
[Click here to see the solution](https://github.com/sudeff/Leetcode-practices/blob/main/Climbing-Stairs/solution)
LeetCode Link:
[Climbing Stairs – LeetCode #70](https://leetcode.com/problems/palindrome-number/)

