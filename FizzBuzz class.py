class Solution:
    def fizzBuzz(self, n: int):
        answer = []
        for i in range(1, n+1):  
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))        
        return answer  

solution = Solution() #created an instance from the class, class cannot be called by itself
print(solution.fizzBuzz(5))