Valid Parentheses

Problem Description:
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is valid.

A string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Every closing bracket has a corresponding open bracket of the same type.

Approach
**Stack-based Matching**
  - Iterate through each character in the string.
  - Push opening brackets to a stack.
  - For each closing bracket, pop from the stack and check if it matches.
  - If the stack is empty at the end and all brackets matched correctly → valid.

Time & Space Complexity
Time Complexity: O(log n)
Because we divide the exponent by 2 at each step.

Space Complexity: O(log n)
Due to recursion stack depth.

Python Code:
[Click here to see the solution](https://github.com/sudeff/Leetcode-practices/blob/main/Valid-Parantheses/solution)

LeetCode Link:
[Valid Parenthesis – LeetCode #20](https://leetcode.com/problems/valid-parentheses/description/)
