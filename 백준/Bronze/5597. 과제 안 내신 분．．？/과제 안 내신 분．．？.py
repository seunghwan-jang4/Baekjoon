students_num = set(range(1, 31))
submmit_students = set()
for i in range(1, 29):
    n = int(input())
    submmit_students.add(n)

bad_students = sorted(students_num - submmit_students)
print(bad_students[0])
print(bad_students[1])