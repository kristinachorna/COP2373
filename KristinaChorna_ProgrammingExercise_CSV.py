# Kristina Chorna
# Programming Exercise CSV
# The objective of this code is to allow the instructor to input the number of students and their information
# and record all their grades


import csv

def write_grades_to_csv():
    filename = 'grades.csv'
    # Prompt the instructor to enter the number of students
    num_students = int(input("Enter the number of students: "))

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        # Get student information
        for i in range(num_students):
            print(f"\nEntering data for student {i + 1}:")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            exam1 = int(input("Exam 1 grade: "))
            exam2 = int(input("Exam 2 grade: "))
            exam3 = int(input("Exam 3 grade: "))
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print(f"\nData has been written to {filename}")

# call function
write_grades_to_csv()



def read_and_display_grades():
    filename = 'grades.csv'

    # Open the CSV file for reading
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)

        # print the results
        print("\nStudent Grades:")
        print("{:<15} {:<15} {:<8} {:<8} {:<8}".format(*header))
        print("-" * 60)

        for row in reader:
            print("{:<15} {:<15} {:<8} {:<8} {:<8}".format(*row))

# call function 
read_and_display_grades()
