Intersection of Two Arrays
Problem Description:
Given two integer arrays `nums1` and `nums2`, return **an array of their intersection**.  
Each element in the result must be **unique** and you may return the result in **any order**.


Example

Input: nums1 = [1,2,2,1], nums2 = [2,2]  
Output: [2]

Approach
Loop through each number in nums1

If it exists in nums2 and is not already in our result list, we add it to the intersection_array

This ensures uniqueness

Return the list of common elements

Time & Space Complexity
Metric	Complexity	Explanation
Time Complexity	O(n * m)	For each element in nums1, check in nums2
Space Complexity	O(k)	Where k is the size of the intersection

LeetCode Link:  
[Intersection of Two Arrays – LeetCode #349](https://leetcode.com/problems/intersection-of-two-arrays/description/)
