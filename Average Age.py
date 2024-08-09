def get_student_ages(num_students):
    ages = []
    for i in range(num_students):
        age = int(input(f"Enter age of student {i + 1}: "))
        ages.append(age)
    return ages


def calculate_average_age(ages):
    total_age = sum(ages)
    num_students = len(ages)
    average_age = total_age / num_students
    return average_age


def main():
    while True:
        num_students = int(input("Enter the number of students in the classroom: "))
        student_ages_list = get_student_ages(num_students)
        average_age = calculate_average_age(student_ages_list)

        print("\nStudent Ages:", student_ages_list)
        print("Average Age:", average_age)

        go_again = input("\nDo you want to run another set? (y/n): ")
        if go_again.lower() != 'y':
            break


if __name__ == "__main__":
    main()