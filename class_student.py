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
    function: get_student_info(): Get the student name, surname, average grade and notes when printing the student info
    function: get_student_notes(): Get the student notes
    function: add_grade(): Append a grade to the student's grades
    function: add_note(): Append a grade to the student's notes
    function: update_address(): Update the student's address
    """

    def __init__(self, first_name, last_name):
        # All the info connected to the student
        self.first_name = first_name
        self.last_name = last_name
        self.graduation_year = None
        self.grades_list = []
        self.address_dict = {'Number': None, 'Street': None, 'Town/City': None, 'Postcode': None}
        self.notes_list = []

    def average_grade(self):
        # Return the average over all grades (as a double/float), to 2 decimal places
        if len(self.grades_list) < 1:
            return 'N/A'
        average = float(sum(self.grades_list)) / len(self.grades_list)
        return "{:.2f}".format(average)

    def pass_fail(self):
        # Return if the student passed (average should be over 60)
        average = self.average_grade()
        if float(average) == 60 or float(average) > 60:
            return 'Pass'
        else:
            return 'Fail'

    def get_student_info(self):
        # Get the student name, surname, average grade and notes when printing the student info.
        # If no notes, return N/A
        if len(self.notes_list) > 0:
            notes = (f"{self.first_name} {self.last_name}, Average Grade: {self.average_grade()}, "
                     f"Notes: {self.notes_list}")
        else:
            notes = f"{self.first_name} {self.last_name}, Average Grade: {self.average_grade()}, Notes: N/A"
        return notes

    def get_student_notes(self):
        # Get the student notes
        if len(self.notes_list) > 0:
            return "No Notes"
        else:
            return self.notes_list

    def add_grade(self, grade):
        # Append a grade to the student's grades
        self.grades_list.append(grade)

    def add_note(self, note):
        # Append a grade to the student's notes
        self.notes_list.append(note)

    def update_address(self, number, street, town_city, postcode):
        # Update the student's address
        self.address_dict['Number'] = number
        self.address_dict['Street'] = street
        self.address_dict['Town/City'] = town_city
        self.address_dict['Postcode'] = postcode

# Test Details
# student1 = Student("John", "Sheridan", 2003, [34, 56, 89, 73, 67])
# student2 = Student("Wolfgang", "Amadeus", 1770, [13, 47, 36, 77])
