[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=5384455&assignment_repo_type=AssignmentRepo)
# Exercise 4.14 Multiplier

Create a class Multiplier that has a:

- Constructor `def __init__(self, number)`.
- Method `def multiply(self, number)` which returns the value `number` passed to it multiplied by the `number` provided to the constructor.

You also need to create an instance variable in this exercise.

An example of the class in use:

```python
multiply_by_three = Multiplier(3)

print("multiply_by_three.multiply(2): " + multiply_by_three.multiply(2))

Multiplier multiplyByFour = new Multiplier(4)

print("multiply_by_four.multiply(2): " + multiply_by_four.multiply(2))
print("multiply_by_three.multiply(1): " + multiply_by_three.multiply(1))
print("multiply_by_four.multiply(1): " + multiply_by_four.multiply(1))
```

Output:

```plaintext
multiply_by_three.multiply(2): 6
multiply_by_four.multiply(2): 8
multiply_by_three.multiply(1): 3
multiply_by_four.multiply(1): 4
```
