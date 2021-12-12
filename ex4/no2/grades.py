

def students_read():
    """
    Reads students names from file and splitting the data to a dictionary
    :return: Dictionary from student's ids to name
    """
    with open("students.txt", "r") as students_file:
        dic = {line.split()[0]: " ".join(line.split()[1:]) for line in students_file.readlines()}
    return dic


def grades_read():
    """
    Reads student's grades from file and splitting the data to a dictionary
    :return: Dictionary from student's ids to grades
    """
    with open("grades.txt", "r") as students_file:
        dic = {line.split()[0]: list(map(int, line.split()[1:])) for line in students_file.readlines()}
    return dic


def max_avg_student(students_names_by_id, students_grades_by_id):
    """
    Finds the student with the highest grades average
    :param students_names_by_id: Student's names by id dictionary
    :param students_grades_by_id: Student's grades by id dictionary
    :return: The name and the average grades of the highest student
    """
    max_avg = (0, "")
    for student in students_names_by_id:
        avg = sum(students_grades_by_id[student]) / len(students_grades_by_id[student])
        if avg > max_avg[0]:
            max_avg = (avg, students_names_by_id[student])
    return max_avg


def max_grades_count(students_names_by_id, students_grades_by_id):
    """
    Finds the grades that appeared the most in student's grades
    :param students_names_by_id: Student's names by id dictionary
    :param students_grades_by_id: Student's grades by id dictionary
    :return: All the grades the appeared the most and their count
    """
    grades_count_by_grades = {}
    for student in students_names_by_id:
        for grade in students_grades_by_id[student]:
            if grade in grades_count_by_grades:
                grades_count_by_grades[grade] += 1
            else:
                grades_count_by_grades[grade] = 1

    max_grade = []
    count = 0
    for grade in grades_count_by_grades:
        if grades_count_by_grades[grade] == count:
            max_grade.append(grade)
            count = grades_count_by_grades[grade]
        if grades_count_by_grades[grade] > count:
            max_grade.clear()
            max_grade.append(grade)
            count = grades_count_by_grades[grade]
    return max_grade, count


def grades_not_presents(students_grades_by_id):
    """
    Finds the grades (from 0  to 100) that did not appear in the student's grades
    :param students_grades_by_id: Student's grades by id dictionary
    :return: Missing grades
    """
    grades = {i for i in range(101)}
    for student_grades in students_grades_by_id.values():
        for grade in student_grades:
            if grade in grades:
                grades.remove(grade)
    return grades


def validate_students_names_by_id(students_names_by_id):
    """
    :param students_names_by_id: Student's names by id dictionary
    :return: True if id and names are valid, otherwise, False
    """
    for student_id in students_names_by_id:
        if not validate_id(student_id) or students_names_by_id[student_id] == "":
            return False
    return True


def validate_students_grades_by_id(students_grades_by_id):
    """
    :param students_grades_by_id: Student's grades by id dictionary
    :return: True if id and grades are valid, otherwise, False
    """
    for student_id in students_grades_by_id:
        if not validate_id(student_id) or students_grades_by_id[student_id] == []:
            return False
    return True


def validate_id(student_id):
    """
    :param student_id: A student id
    :return: True if the student id is a valid id, otherwise False
    """
    return len(student_id) == 9


def main():
    """
    Main logic func: reads students data, validating the data and printing:
    The student with the highest average grade
    The most appearing grades
    List of all the grades that did not appear in any student
    """
    try:
        students_names_by_id = students_read()
    except IOError as e:
        print(f"Could not open file: {e.filename}")
        return
    except Exception:
        print("Invalid data in student's names file")
        return
    try:
        students_grades_by_id = grades_read()
    except IOError as e:
        print(f"Could not open file: {e.filename}")
        return
    except Exception:
        print("Invalid data in student's grades file")
        return

    if not validate_students_names_by_id(students_names_by_id):
        print("Invalid data in student's names file")
        return
    if not validate_students_grades_by_id(students_grades_by_id):
        print("Invalid data in student's grades file")
        return
    if students_names_by_id.keys() != students_grades_by_id.keys():
        print("Some student's ids are missing!")
        return

    max_avg = max_avg_student(students_names_by_id, students_grades_by_id)
    print(f"Best student: {max_avg[1]}, average: {max_avg[0]:.2f}")

    max_grades, count = max_grades_count(students_names_by_id, students_grades_by_id)
    print(f"The grade {', '.join([str(t) for t in max_grades])} appeared {count} times")

    missing_grades = grades_not_presents(students_grades_by_id)
    print(f"The grades that did not appear:")
    print(list(missing_grades))


if __name__ == '__main__':
    main()
