# Provide code that:
# A. Creates objects and shows the functionality.
# B. Asks for user input to:
#     - Add a new student
#     - Add a new grade to a student
#     - Add a student to a classroom
#     - Remove a student from the classroom
#     - Print all grade averages for a classroom
#     - Print the total average for a classroom

from class_classroom import Classroom
from class_student import Student

def create_new_classroom():
    # Create a new object from Class classroom with attributes for Class ID and Max class size.
    room_id = input('Insert new classroom ID, eg. room_01, room_02: ')
    max_room_size = input('Insert new classroom maximum size, eg 20, 25: ')
    new_classroom = Classroom(room_id, max_room_size)
    print('New Class Created')

    # Create a new object from Class student with attributes for first and last name, then add to class register
    yes_no = input('Would you like to add a student? Y / N ')
    new_stu_fname = ''
    new_stu_lname = ''
    if yes_no in ['N', 'n']:
        return
    elif yes_no in ['Y', 'y']:
        new_stu_fname = input('Firstname: ')
        new_stu_lname = input('Lastname: ')

        new_student = Student(new_stu_fname, new_stu_lname)
        print(Student.get_student_info(new_student))
        new_classroom.add_student_to_classroom()

        print(new_classroom.get_class_register())

print(create_new_classroom())


# Tests needed:
#  if room ID does not meet criteria
#  if class max size not int
#  if add new stu not Y/N
