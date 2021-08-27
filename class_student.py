
class Student:
    """Create a class Student that keeps records of students, and functions to be used upon it.
    
    param: first name (str)
    param: last name (str)
    param: graduation year (int) (if student graduated, otherwise leave empty)
    param: grades_list (list of int) (each grade an int between 1 and 100)
    param: address_list (list of str) [number, street, town_city, country, postcode]
    param: notes (list of str)

    function: average_grade(): Return the average over all grades (as a double)
    function: pass_fail(): Return if the student passed (average should be over 60)
    function: print_stud_info(): Get the student name, surname, average grade and notes when printing the student info
    function: student_notes(): Get the student notes
    function: add_grade(): Append a grade to the student's grades
    function: add_note(): Append a grade to the student's notes
    function: update_address(): Update the student's address

    """

    def __init__(self, first_name, last_name, graduation_year, grades_list, address_list, notes):
        # All the info connected to the student
        self.first_name = first_name
        self.last_name = last_name
        self.graduation_year = graduation_year
        self.grades_list = grades_list
        self.address_list = address_list
        self.notes = notes

    def average_grade(grades_list):
    # Return the average over all grades (as a double)
        total = 0
        for grade in grades_list:
            float(grade)
            total = total + grade
        average = total / len(grades_list)
        return "{:.2f}".format(average)

    def pass_fail(grades_list):
        # Return if the student passed (average should be over 60)
        average = Student.average_grade(grades_list)
        if float(average) == 60 or float(average) > 60:
            return 'Pass'
        else: return 'Fail'
        
    def print_stud_info(student_number):
        # Get the student name, surname, average grade and notes when printing the student info
        

        print(f"{student1.first_name} {student1.last_name}, Average Grade: {Student.average_grade(student1.grades_list)}, Result: {Student.pass_fail(student1.grades_list)}")
        

    def student_notes():
        # Get the student notes
        pass

    def add_grade():
        # Append a grade to the student's grades
        pass

    def add_note():
        # Append a grade to the student's notes
        pass

    def update_address():
        # Update the student's address
        pass


student1 = Student("John", "Sheridan", 2003, [34, 56, 89, 73, 67], ["42", "Locatia Drive", "Springfield", "Wales", "SA72 8OD" ], ["Maintains a good standard. Could focus more on the task at hand rather than planning ahead all the time."])
student2 = Student("Wolfgang", "Amadeus", 1770, [13, 47, 36, 77], ["43", "Violin Street", "Vienna", "V1 QWERTY"], ["Excellent at improvising. Often forgets to take breats / sleep."])

print(Student.average_grade(student1.grades_list))
print(Student.pass_fail(student1.grades_list))
print(Student.average_grade(student2.grades_list))
print(Student.pass_fail(student2.grades_list))

# Use format to return name, average grade and pass/fail
print(f"{student1.first_name} {student1.last_name}, Average Grade: {Student.average_grade(student1.average_grade)}, Result: {Student.pass_fail(student1.average_grade)}")


