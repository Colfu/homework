class Student:
    """Create a class Student that keeps records of students, and functions to be used upon it.

    param: first name (str)
    param: last name (str)
    param: graduation year (int) (if student graduated, otherwise leave empty)
    param: grades_list (list of int) (each grade an int between 1 and 100)
    param: address_list (list of str) [number, street, town_city, country, postcode]
    param: notes (list of str)

    function: add_grade(grade): Append a grade to the student's grades
    function: average_grade(): Return the average over all grades (as a double)
    function: pass_fail(): Return if the student passed (average should be over 60)
    function: add_note(note): Append a note to the student's notes
    function: get_student_notes(): Get the student notes
    function: update_address(number, street, town_city, postcode): Update the student's address
    function: get_student_info(): Get the student name, surname, average grade and notes when printing the student info

    """

    def __init__(self, first_name, last_name):
        # All the info connected to the student
        self.first_name = first_name
        self.last_name = last_name
        self.graduation_year = None
        self.grades_list = []
        self.address_dict = {'Number': None, 'Street': None, 'Town/City': None, 'Postcode': None}
        self.notes_list = []

    def __str__(self):
        # returns the following string when the object is printed
        return f'{self.first_name} {self.last_name}, Grade: {self.average_grade()}'

    def __repr__(self):
        return f'Student(first_name={self.first_name}, last_name={self.last_name}, ' \
               f'average_grade={self.average_grade()})'

    def add_grade(self, grade):
        # Append a grade to the student's grades
        self.grades_list.append(grade)
        return f'Grade {grade} added to {self.first_name} {self.last_name}'

    def average_grade(self):
        # Return the average over all grades (as a double/float), to 2 decimal places
        if len(self.grades_list) < 1:
            return 'N/A'
        average = float(sum(self.grades_list)) / len(self.grades_list)
        return "{:.2f}".format(average)

    def pass_fail(self):
        # Return if the student passed (average should be over 60)
        average = self.average_grade()
        if len(self.grades_list) < 1:
            return 'N/A'
        elif float(average) == 60 or float(average) > 60:
            return 'Pass'
        else:
            return 'Fail'

    def add_note(self, note):
        # Append a grade to the student's notes
        self.notes_list.append(note)
        return 'Note Added'

    def get_student_notes(self):
        # Get the student notes
        if len(self.notes_list) == 0:
            return "No Notes"
        else:
            return self.notes_list

    def update_address(self, number, street, town_city, postcode):
        # Update the student's address
        self.address_dict['Number'] = number
        self.address_dict['Street'] = street
        self.address_dict['Town/City'] = town_city
        self.address_dict['Postcode'] = postcode
        return 'Address Updated'

    def get_student_info(self):
        # Get the student name, surname, average grade and notes when printing the student info.
        # If no notes, return N/A
        if len(self.notes_list) > 0:
            notes = (f"{self.first_name} {self.last_name}, Average Grade: {self.average_grade()}, "
                     f"Notes: {self.notes_list}")
        else:
            notes = f"{self.first_name} {self.last_name}, Average Grade: {self.average_grade()}, Notes: N/A"
        return notes





#Basic Testing
# bob_dylan = Student('Bob', 'Dylan')
#
# print('Test bob_dylan.first_name: ', bob_dylan.first_name)
#
# print('Test bob_dylan.last_name: ', bob_dylan.last_name)
# print('Test bob_dylan.graduation_year: ', bob_dylan.graduation_year)
# print('Test bob_dylan.grades_list: ', bob_dylan.grades_list)
# print('Test bob_dylan.address_dict: ', bob_dylan.address_dict)
# print('Test bob_dylan.notes_list: ', bob_dylan.notes_list)
# print('')
# print('Test_Function bob_dylan: ', bob_dylan)
# print('Test_Function str(bob_dylan): ', str(bob_dylan))
# print('Test_Function repr(bob_dylan): ', repr(bob_dylan))
# print('')
# print('Test_Function bob_dylan.average_grade():', bob_dylan.average_grade())
# print('Test_Function bob_dylan.add_grade(grade):', bob_dylan.add_grade(50))
# print('Test_Function bob_dylan.add_grade(grade):', bob_dylan.add_grade(25))
# print('Test_Function bob_dylan.add_grade(grade):', bob_dylan.add_grade(75))
# print('Test bob_dylan.grades_list: ', bob_dylan.grades_list)
# print('Test_Function bob_dylan.average_grade():', bob_dylan.average_grade())
# print('Test_Function bob_dylan.pass_fail():', bob_dylan.pass_fail())
# print('')
# print('Test_Function bob_dylan.add_note("This is a note."):', bob_dylan.add_note('This is a note.'))
# print('Test_Function bob_dylan.add_note("And this is another note"):', bob_dylan.add_note('And this is another note.'))
# print('Test_Function bob_dylan.get_student_notes():', bob_dylan.get_student_notes())
# print('Test_Function bob_dylan.update_address(43, "Bob\'s Street, "Dylan Town", "BD01 BOB"):',
#       bob_dylan.update_address(43, 'Bob"s Street', 'Dylan Town', 'BD01 BOB'))
# print('Test_Function bob_dylan.get_student_info():', bob_dylan.get_student_info())
