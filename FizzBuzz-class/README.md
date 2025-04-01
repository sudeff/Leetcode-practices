FizzBuzz

Problem Description:
For numbers from 1 through n:
- If a number is divisible by 3 → output `"Fizz"`.
- If a number is divisible by 5 → output `"Buzz"`.
- If a number is divisible by both 3 and 5 → output `"FizzBuzz"`.
- Otherwise, output the number itself.

Approaches
1. Print Directly (O(1) Space)  
   - Simply loop from 1 to n, decide the output for each number, and print immediately.  

2. Store in a List (O(n) Space) 
   - Loop from 1 to n, build a list of the results, then return/print at the end.  

Time & Space Complexity
- Time Complexity: O(n) — we must check each number from 1 to n.
- Space Complexity:
  - O(1): extra space if we just print results (no data structure).
  - O(n): if we store all results in a list before returning/printing.
  
Python Code:
[Click here to see the solution](https://github.com/sudeff/Leetcode-practices/blob/main/FizzBuzz_class/FizzBuzz%20class.py)

LeetCode Link:
[FizzBuzz – LeetCode #412](https://leetcode.com/problems/fizz-buzz/description/)
