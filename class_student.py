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
    function: get_student_notes(): Get the student notes
    function: add_grade(): Append a grade to the student's grades
    function: add_note(): Append a grade to the student's notes
    function: update_address(): Update the student's address

    """

    def __init__(self, first_name, last_name, graduation_year, grades_list):
        # All the info connected to the student
        self.first_name = first_name
        self.last_name = last_name
        self.graduation_year = graduation_year
        self.grades_list = grades_list
        self.address_list = []
        self.notes_list = []

    def average_grade(self):
        # Return the average over all grades (as a double), to 2 decimal places
        average = float(sum(self.grades_list)) / len(self.grades_list)
        return "{:.2f}".format(average)

    def pass_fail(self):
        # Return if the student passed (average should be over 60)
        average = self.average_grade()
        if float(average) == 60 or float(average) > 60:
            return 'Pass'
        else:
            return 'Fail'

    def print_stud_info(self):
        # Get the student name, surname, average grade and notes when printing the student info.
        # If no notes, return N/A
        if len(self.notes_list) > 0:
            notes = (f"{self.first_name} {self.last_name}, Average Grade: {self.average_grade()}, "
                     f"Notes: {self.notes_list}")
        else:
            notes = f"{self.first_name} {self.last_name}, Average Grade: {self.average_grade()}, Notes: N/A"
        return notes

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


student1 = Student("John", "Sheridan", 2003, [34, 56, 89, 73, 67])
student2 = Student("Wolfgang", "Amadeus", 1770, [13, 47, 36, 77])

# Use format to return name, average grade and pass/fail
# print(f"{student1.first_name} {student1.last_name}, Average Grade: "
#       f"{student1.average_grade()}, Result: {student1.pass_fail()}")
# print(f"{student2.first_name} {student2.last_name}, Average Grade: "
#       f"{student2.average_grade()}, Result: {student2.pass_fail()}")

print(student1.print_stud_info())
