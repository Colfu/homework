# Q: How to connect this to the Students made using Student Class
#  need to change add_stdent() to use Student Class objects?
class Classroom:
    """
    Create a class Classroom that keeps records of students (as objects of the
    class Student)

    param: room_id:  classroom id (as a string of numbers and letters)
    param: max_classroom_size:  max classroom size (int)
    param: current_classroom_size:  current classroom size (int)
    param: register_list:  a list of dictionaries (firstname, lastname, average grade) to keep records of all students
    in that classroom

    function: add_current_classroom_size() - replace with get_current_room_size()
    function: get_students_average_grades(): the average grade of each student that belongs to the classroom
    function: get_classroom_average_grade(): the total average grade of the class
    function: add_student_to_classroom(): add student entry
    function: remove_student_from_classroom(): remove student by providing the first name and the last name
    function: get_classroom_id(): get the classroom id
    """

    def __init__(self, classroom_id, max_classroom_size):
        # All the info connected to the classroom
        self.classroom_id = classroom_id
        self.max_classroom_size = max_classroom_size
        self.current_classroom_size = 0
        self.register_list = []

    def add_current_room_size(self, current_size):
        # Not needed - see get_current_room_size function which is a better way of getting the information
        self.current_classroom_size = current_size

    def get_current_classroom_size(self):
        if len(self.register_list) == 0:
            return 'Class Empty'
        else:
            return len(self.register_list)

    def get_students_average_grades(self):
        for student_dict in self.register_list:
            fn = student_dict.get('Firstname')
            ln = student_dict.get('Lastname')
            avg = student_dict.get('Average Grade')
            print(f'{fn} {ln}, Av.Grade: {avg}')
        return ' '

    def get_classroom_average_grade(self):
        total = 0
        for student_dict in self.register_list:
            if student_dict.get('Average Grade') is None:
                continue
            else:
                total += student_dict.get('Average Grade')
        return total/len(self.register_list)

    def add_student(self, firstname, lastname):
        # Adding a student to the register, unless class is already full
        if self.current_classroom_size == self.max_classroom_size:
            print('Sorry, this class is already full.')
        else:
            student_dict = {'Firstname': firstname, 'Lastname': lastname, 'Average Grade': None}
            self.register_list.append(student_dict)

    def remove_student_from_classroom(self, firstname, lastname):
        for student_dict in self.register_list:
            if student_dict.get('Firstname') == firstname and student_dict.get('Lastname') == lastname:
                self.register_list.remove(student_dict)
            else:
                continue

    def get_classroom_id(self):
        return self.classroom_id

# Test Data:
# room_01 = Classroom("room_01", 25)
# # room_02 = Classroom("room_02", 40)
#
# room_01.add_student('Andy', 'Sheridan')
# room_01.add_student('Bob', 'Sheridan')
# room_01.add_student('Craig', 'James')
# room_01.add_student('Dan', 'Archibald')

