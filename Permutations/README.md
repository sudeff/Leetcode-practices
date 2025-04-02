Permutations

Problem Description:

Given an array `nums` of distinct integers, return **all the possible permutations**. You can return the answer in any order.

Example:
Input: nums = [1, 2, 3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

Approach:
Each permutation build step by step using a recursive backtrack function.

A used list keeps track of which elements have already been added to the current path.

When the path has the same length as the input nums, it means a full permutation is formed and added to the result list.

After each recursive call, backtrack applied: unmark the used element to explore other possibilities.

Time & Space Complexity:
Time	O(n × n!) — n! permutations generated and each takes O(n) to build
Space	O(n) for recursion stack + O(n) for used list per call

Python Code:
[Click here to see the solution](https://github.com/sudeff/Leetcode-practices/blob/main/Permutations/solution)

LeetCode Link:
[Permutations – LeetCode #46](https://leetcode.com/problems/permutations/description/)
