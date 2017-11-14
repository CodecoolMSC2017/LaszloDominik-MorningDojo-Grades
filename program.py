#!/bin/python3
import sys


def solve(grades):
    roundedGrades = []
    for i in grades:
        if i < 38:
            roundedGrades.append(i)
        elif i % 5 < 3:
            roundedGrades.append(i)
        elif i % 5 >= 3:
            roundedGrades.append(i + (5 - i % 5))
    return roundedGrades


n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
print("\n".join(map(str, result)))
