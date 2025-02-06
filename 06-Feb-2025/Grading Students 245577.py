# Problem: Grading Students - https://www.hackerrank.com/challenges/grading/problem

def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        dif = 5 - (grades[i] % 5)
        if dif < 3 and grades[i] >37:
            grades[i] +=  dif
    return grades
