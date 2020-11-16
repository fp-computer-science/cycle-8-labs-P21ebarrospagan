# Author: EBP (AMDG) 11/16/20

subjects = ["Math", "Science" "Computer Science"]
print(subjects)

subjects.append("Spanish")
print(subjects)

print(subjects.index('Computer Science'))

subjects.sort()
print(subjects)

more_subjects = subjects.copy()

more_subjects.reverse()
print(more_subjects)