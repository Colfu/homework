from class_classroom import Classroom
from class_student import Student


def create_new_classroom():
    # Create a new object from Class classroom with attributes for Class ID and Max class size.
    room_id = input('Insert new classroom ID, eg. room_01, room_02: ')
    max_room_size = input('Insert new classroom maximum size, eg 20, 25: ')
    new_classroom = Classroom(room_id, max_room_size)

    # Create a new object from Class student with attributes for first and last name, then add to class register
    yes_no = input('Would you like to add a student? Y / N ')
    new_stu_fname = ''
    new_stu_lname = ''
    if yes_no in ['N', 'n']:
        pass
    elif yes_no in ['Y', 'y']:
        new_stu_fname = input('Firstname: ')
        new_stu_lname = input('Lastname: ')

        new_student = Student(new_stu_fname, new_stu_lname)
        new_classroom.add_student_to_classroom(new_student)
        print('New Student Added')

        print(new_classroom.get_class_register())

        reg_list = new_classroom.get_class_register()
        for student in reg_list:
            print(student)



print(create_new_classroom())
