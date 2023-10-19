# Leetcode # 1491. Average Salary Excluding the Minimum and Maximum Salary

class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary, max_salary = 1e6, 1000
        total = 0
        for now_salary in salary:
            total += now_salary
            if now_salary < min_salary:
                min_salary = now_salary
            if now_salary > max_salary:
                max_salary = now_salary
        return (total - min_salary - max_salary) / (len(salary) - 2)