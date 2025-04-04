[Fibonacci-number – LeetCode #509](https://leetcode.com/problems/majority-element/description/)


For this exercise 2 approaches are used. In the first one, each element in the list is compared with the other elements and if that element is more than half the length of the list, it is returned. Since the if loop is used twice in this approach, the time complexity is O(n^2).
In the other approach, we determine a candidate for the number we are looking for and increase the count by one every time we encounter that number in the list and decrease it by one when we encounter another number. When the count exceeds n/2, we find it. Here, the time complexity is O(n). In other words, it works more efficiently than the first approach.
