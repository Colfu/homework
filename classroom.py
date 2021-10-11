
from student import Student


class Classroom:
    """
    Create a class Classroom that keeps records of students (as objects of the
    class Student)

    param: room_id:  classroom id (as a string of numbers and letters)
    param: max_classroom_size:  max classroom size (int)
    param: current_classroom_size:  current classroom size (int)
    param: register_list:  a list of dictionaries (firstname, lastname, average grade) to keep records of all students
    in that classroom
### Can this be a list of (Student) objects instead? Do I nee the equivalent
            of a variable that points to each object (eg. a student ID)?

    function: get_current_room_size(): return amount of students currently in the classroom
    function: add_student_to_classroom(): add student entry to class register
    function: get_class_register(): return the class register list
### The above function will need to change if the register becomes list of objects.
            Will need to return specific details from object
    function: remove_student_from_classroom(): remove student by providing the first name and the last name
### The above function will need to change if the register becomes list of objects.

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

    def add_student_to_classroom(self, firstname, lastname, average_grade=0):
        # Adding a student to the register, unless class is already full
        if len(self.register_list) == self.max_classroom_size:
            print('Sorry, this class is already full.')
        else:
            self.register_list.append([firstname, lastname, average_grade])

    def get_class_register(self):
        return self.register_list

    def remove_student_from_classroom(self, firstname, lastname):   # remove student not 1st/last name
        for student in self.register_list:
            if student.first_name == firstname and student.last_name == lastname:
                self.register_list.remove(student)
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
room_01 = Classroom("room_01", 25)
room_02 = Classroom("room_02", 40)

# Basic Testing:

print(room_01.get_current_classroom_size())
# add_student_to_classroom()
room_01.add_student_to_classroom('Andy', 'Sheridan')
room_01.add_student_to_classroom('Bob', 'Sheridan', 46)
room_01.add_student_to_classroom('Craig', 'James')
room_01.add_student_to_classroom('Dan', 'Archibald', 87)
print(room_01.get_current_classroom_size())
print(room_01.get_class_register())


# remove_student_from_classroom()
# get_students_average_grades()
# get_classroom_average_grade()
# get_classroom_id()

