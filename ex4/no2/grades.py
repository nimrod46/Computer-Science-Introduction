import math


def students_read():
    with open("students.txt", "r") as students_file:
        dic = {line.split()[0]: " ".join(line.split()[1:]) for line in students_file.readlines()}
        return dic


def grades_read():
    with open("grades.txt", "r") as students_file:
        dic = {line.split()[0]: list(map(int, line.split()[1:])) for line in students_file.readlines()}
        return dic


def max_avg_student(students_names_by_id, students_grades_by_id):
    max_avg = (0, "")
    for student in students_names_by_id:
        avg = sum(students_grades_by_id[student]) / len(students_grades_by_id[student])
        if avg > max_avg[0]:
            max_avg = (avg, students_names_by_id[student])
    return max_avg


def max_grades_count(students_names_by_id, students_grades_by_id):
    grades_count_by_grades = {}
    for student in students_names_by_id:
        for grade in students_grades_by_id[student]:
            if grade in grades_count_by_grades:
                grades_count_by_grades[grade] += 1
            else:
                grades_count_by_grades[grade] = 1

    max_grade = [(0, 0)]
    for grade in grades_count_by_grades:
        if grades_count_by_grades[grade] == max_grade[0][1]:
            max_grade.append((grade, grades_count_by_grades[grade]))
        if grades_count_by_grades[grade] > max_grade[0][1]:
            max_grade.clear()
            max_grade = [(0, 0)]
            max_grade[0] = (grade, grades_count_by_grades[grade])
    return max_grade


def grades_not_presents(students_grades_by_id):
    grades = {i for i in range(101)}
    for student_grades in students_grades_by_id.values():
        for grade in student_grades:
            if grade in grades:
                grades.remove(grade)
    return grades


def validate_students_names_by_id(students_names_by_id):
    for student_id in students_names_by_id:
        if not validate_id(student_id) or students_names_by_id[student_id] == "":
            return False
    return True


def validate_students_grades_by_id(students_grades_by_id):
    for student_id in students_grades_by_id:
        if not validate_id(student_id) or students_grades_by_id[student_id] == []:
            return False
    return True


def validate_id(student_id):
    return len(student_id) == 9


def main():
    try:
        students_names_by_id = students_read()
        students_grades_by_id = grades_read()
    except Exception as e:
        print("Error reading students data: " + str(e))
        return

    if not validate_students_names_by_id(students_names_by_id):
        print("Failed validating student's names data")
        return
    if not validate_students_grades_by_id(students_grades_by_id):
        print("Failed validating student's grades data")
        return
    if students_names_by_id.keys() != students_grades_by_id.keys():
        print("Some student's ids are missing!")
        return

    max_avg = max_avg_student(students_names_by_id, students_grades_by_id)
    print(f"Best student: {max_avg[1]}, average: {max_avg[0]}")

    max_grades = max_grades_count(students_names_by_id, students_grades_by_id)
    print(f"The grade {', '.join([str(t[0]) for t in max_grades])} appeared {max_grades[0][1]} times")

    missing_grades = grades_not_presents(students_grades_by_id)
    print(f"The grades that did not appear:")
    print(list(missing_grades))


if __name__ == '__main__':
    main()
