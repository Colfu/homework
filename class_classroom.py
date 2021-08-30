# Notes
# - need to complete functions
# - need to import class student so can use its functions within these functions to connect

class Classroom:
    """
    Create a class Classroom that keeps records of students (as objects of the
    class Student)

    param: room_id:  classroom id (as a string of numbers and letters)
    param: max_room_size:  max classroom size (int)
    param: current_room_size:  current classroom size (int)
    param: register_list:  a list of dictionaries (firstname, lastname, average grade) to keep records of all students
    in that classroom

    function: add_current_room_size
    function: print_students_average_grades: print the average grade of each student that belongs to the classroom
    function: print_class_average_grade: print the total average grade of the class
    function: add_student_to_class: add student entry
    function: remove_student_from_class: remove student by providing the first name and the last name
    function: get_class_id: get the classroom id
    """

    def __init__(self, room_id, max_room_size):
        # All the info connected to the classroom
        self.room_id = room_id
        self.max_room_size = max_room_size
        self.current_room_size = 0
        self.register_list = [{'Firstname': None, 'Lastname': None, 'Average Grade': None}]

    def add_current_room_size(self, current_size):
        # Not needed - see get_current_room_size function. This would
        self.current_room_size = current_size

    def get_current_room_size(self):
        return len(self.register_list)

    def print_students_average_grades(self):
        return self.register_list

    def print_class_average_grade(self):
        total = 0
        for student_dict in self.register_list:
            total += student_dict['Average Grade']
        return total

    def add_student(self, firstname, lastname):
        pass

    def remove_student_from_class(self, firstname, lastname):
        pass

    def get_class_id(self):
        pass


# Test Data:
room_01 = Classroom("room_01", 25)
room_02 = Classroom("room_02", 40)
