
from school import School


class Classroom:
    """
    Create a class Classroom that keeps records of students (as objects of the
    class Student)

    param: room_id:  classroom id (as a string of numbers and letters)
    param: max_classroom_size:  max classroom size (int)
    param: current_classroom_size:  current classroom size (int)
    param: register_list:  a list of dictionaries (firstname, lastname, average grade) to keep records of all students
    in that classroom
### Can this be a list of (Student) objects instead? Do I need the equivalent
            of a variable that points to each object (eg. a student ID)?

    function: get_current_room_size(): return amount of students currently in the classroom
    function: add_student_to_classroom(): add student entry to class register
    function: get_class_register(): return the class register list
    function: remove_student_from_classroom(): remove student by providing the first name and the last name
    function: get_students_average_grades(): return the average grade of each student that belongs to the classroom
    function: get_classroom_average_grade(): return the total average grade of the class
    function: get_classroom_id(): return the classroom id

    """

    def __init__(self, classroom_id, max_classroom_size):
        # All the info connected to the classroom
        self.classroom_id = classroom_id
        self.max_classroom_size = max_classroom_size
        self.register_list = []

    def get_current_classroom_size(self):
        if len(self.register_list) == 0:
            return 'Class Empty'
        else:
            return len(self.register_list)

    def add_student_to_classroom(self, firstname, lastname):
        # Adding a student to the register, unless class is already full
        if len(self.register_list) == self.max_classroom_size:
            print('Sorry, this class is already full.')
        else:
            # find student in School list and add them to this class register
            for student in School.school_student_list():
### self is referring to the clas srather than the object. How do I refer to the object when it's not created yet?
                if student.first_name == firstname and student.last_name == lastname:
                    self.register_list.append(student)
                    return f'{student.first_name} {student.last_name} added to class'

    def get_class_register(self):
        for student in self.register_list:
            return f'Name: {student.first_name} {student.last_name}, Av.Grade: {student.average_grade()}'

    def remove_student_from_classroom(self, firstname, lastname):
        for student in self.register_list:
            if student.first_name == firstname and student.last_name == lastname:
                self.register_list.remove(student)
                return f'{student.first_name} {student.last_name} removed from class'
            else:
                continue

    def get_students_average_grades(self):
        for student in self.register_list:
            fn = student.first_name
            ln = student.last_name
            avg = student.average_grade()
            print(f'{fn} {ln}, Av.Grade: {avg}')
        return ' '

    def get_classroom_average_grade(self):
        total = 0
        for student in self.register_list:
            if student.average_grade() is None:
                continue
            else:
                total += student.average_grade()
        return total/len(self.register_list)

    def get_classroom_id(self):
        return self.classroom_id


# Test Data:
# room_01 = Classroom("room_01", 25)
# room_02 = Classroom("room_02", 40)
