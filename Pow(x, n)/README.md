Pow(x, n)
Problem:
Implement the function `myPow(x, n)` which calculates `x^n` (x raised to the power of n). Do **not** use built-in library functions like `pow()`.
- `x` is a double.
- `n` is an integer.
- Handle both positive and negative exponents.

Constraints:
- `-100.0 < x < 100.0`
- `-2^31 <= n <= 2^31 - 1`
- The result must be within the range `[-10^4, 10^4]`.

Approach:
Recursive Fast Exponentiation (Divide and Conquer)
If n == 0, return 1 (base case).

If n < 0, compute the reciprocal: myPow(1/x, -n)

If n is even: calculate myPow(x * x, n // 2)

If n is odd: multiply once with x → x * myPow(x, n - 1)

Example:
Input: x = 2.00000, n = 10
Output: 1024.00000

Time & Space Complexity
Time Complexity: O(log n)
Because the problem size is halved at each recursive step.

Space Complexity: O(log n)
Due to recursive call stack (can be optimized to O(1) with iteration).

Python Code:
[Click here to see the solution](https://github.com/sudeff/Leetcode-practices/blob/main/Pow(x%2C%20n)/solution.py) 

LeetCode Link:
[Pow(x, n) – LeetCode #50] (https://leetcode.com/problems/powx-n/description/)


