class Student:
    def __init__(self, name, age, grades):
        """Initialize the student with name, age, and a list of grades."""
        self.name = name
        self.age = age
        self.grades = grades  # List of grades
    
    def display_info(self):
        """Display the student's information."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")
    
    def average_grade(self):
        """Calculate the average grade of the student."""
        if len(self.grades) > 0:
            avg = sum(self.grades) / len(self.grades)
            return round(avg, 2)
        else:
            return 0  # If no grades are available


class StudentDatabase:
    def __init__(self):
        """Initialize an empty list to store students."""
        self.students = []
    
    def add_student(self, student):
        """Add a student to the database."""
        self.students.append(student)
    
    def display_all_students(self):
        """Display all students' information and average grades."""
        if not self.students:
            print("No students in the database.")
        else:
            for student in self.students:
                student.display_info()
                print(f"Average Grade: {student.average_grade()}\n")


# Main program to interact with the user
def main():
    # Create a student database object
    database = StudentDatabase()

    # Scenario: Adding and displaying students
    print("Welcome to the Student Database!")

    # Add new students to the database
    student1 = Student("Alice", 20, [85, 90, 92])
    student2 = Student("Bob", 22, [75, 80, 78])
    
    database.add_student(student1)
    database.add_student(student2)

    # Display all students in the database
    print("\nDisplaying all students:")
    database.display_all_students()

    # Allow the user to add another student
    print("Now, let's add a new student.")
    name = input("Enter the student's name: ")
    age = int(input("Enter the student's age: "))
    grades = list(map(int, input("Enter the student's grades (comma separated): ").split(',')))

    new_student = Student(name, age, grades)
    database.add_student(new_student)

    # Display all students again after adding the new one
    print("\nUpdated list of all students:")
    database.display_all_students()


# Run the main function to simulate the program interaction
if __name__ == "__main__":
    main()
