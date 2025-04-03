Remove Duplicates from Sorted Array

Problem Description.

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. After removing the duplicates, return the number of unique elements `k`.

It must be done in-place with `O(1)` extra memory.

Example

The two-pointer technique is used:

1. One pointer (`position_var`) tracks the position where the next unique element should go.
2. Iterate over the array:
   - If the current number is different from the previous one, place it at `position_var` and increment the pointer.

We overwrite duplicates as we go, fulfilling the in-place requirement.

Time & Space Complexity

Time Complexity: O(n)
List is traversed only once.

Space Complexity: O(1)
The operation is done in-place, using only constant space.

LeetCode Link:
[Remove Duplicates from a Sorted Array – LeetCode #26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)