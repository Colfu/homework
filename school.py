from student import Student


class School:
    """
    Create a class School that stores all Students and Classrooms

    param: school_name: Name of the School
    param: school_student_list: list of all students registered in school
    param: school_classroom_list: list of all classes registered in school

    function: get_school_register_list(): returns list of all students registered in the school (first name, last name)
    function: is_student_registered(student_fname, student_lname): takes a student object (first name, last name)
    and returns true if the student is registered
    function: get_student_classes(student_fname, student_lname): takes a student object (first name, last name)
    and returns the classes the student is registered in
    """

    def __init__(self, school_name):
        # All the info connected to the classroom
        self.school_name = school_name
######### need to be able to add Student/Classroom objects to these lists
        self.school_classroom_list = []
        self.school_student_list = []

    def add_student_to_school_student_list(self, student_fname, student_lname):
        self.school_student_list.append(Student(student_fname, student_lname))

    def school_student_list(self):
        return self.school_student_list

    def is_student_registered(self, student_fname, student_lname):
        for student in self.school_student_list:
            if student.fname == student_fname and student.lname == student_lname:
                return f'{student_fname} {student_lname} is registered.'
            else:
                return f'{student_fname} {student_lname} is not registered.'

    def get_student_classes(self, student_fname, student_lname):
        for classroom in self.school_classroom_list:
            for student in self.school_classroom_list:
                if student.fname == student_fname and student.lname == student_lname:
                    print(f'{student_fname} {student_lname} is in {classroom}.')
                else:
                    continue

cambridge_school = School('Cambridge School')
cambridge_school.add_student_to_school_student_list('Bob', 'Dylan')

