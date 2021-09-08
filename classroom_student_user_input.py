# Provide code that:
# A. Creates objects and shows the functionality.
# B. Asks for user input to:
#     - Add a new student   *Cr.1
#     - Add a new grade to a student   *Cr.2
#     - Add a student to a classroom    *Cr.3
#     - Remove a student from the classroom    *Cr.4
#     - Print all grade averages for a classroom    *Cr.5
#     - Print the total average for a classroom     *Cr.6

from class_classroom import Classroom
from class_student import Student


# def create_new_classroom():
#     # Create a new object from Class classroom with attributes for Class ID and Max class size.
#     room_id = input('Insert new classroom ID, eg. room_01, room_02: ')
#     max_room_size = input('Insert new classroom maximum size, eg 20, 25: ')
#     new_classroom = Classroom(room_id, max_room_size)

    # Create a new object from Class student with attributes for first and last name, then add to class register
        #     yes_no = input('Would you like to add a student? Y / N ')
        #     new_stu_fname = ''
        #     new_stu_lname = ''
        #     if yes_no in ['N', 'n']:
        #         pass
        #     elif yes_no in ['Y', 'y']:
        #         new_stu_fname = input('Firstname: ')
        #         new_stu_lname = input('Lastname: ')
        #
        #         new_student = Student(new_stu_fname, new_stu_lname)
        #         new_classroom.add_student_to_classroom(new_student)
        #         print('New Student Added')
        #
        #         # print(new_classroom.get_class_register())      !!This isn't correct!!

# print(create_new_classroom())

# set up loop for options menu
continue_yes_no = 1
while continue_yes_no == 1:
    #  Ask what function the user would like to do
    option = input('\nWhat would you like to do? '
                    '\n1: Add new classroom'
                    '\n2: Add new student'
                    '\n3: Add new grade to student'
                    '\n4: Add student to classroom'
                    '\n5: Remove student from classroom'
                    '\n6: Print grade averages for classroom'
                    '\n7: Print total average for classroom'
                    '\nQ: Quit'
                    '\nChoose your option: ')
    if option in ['q', 'Q']:
        break
    else:
        option = int(option)

    if option == 1:
        # Create new classroom
        room_id = input('Insert new classroom ID, eg. room_01, room_02: ')
        max_room_size = input('Insert new classroom maximum size, eg 20, 25: ')
        new_classroom = Classroom(room_id, max_room_size)
        print('New Class Created')
    elif option == 2:
        # Create new student                *** but where is this 'stored' to be accessed if not in a register?
        new_stu_fname = input('Firstname: ')
        new_stu_lname = input('Lastname: ')
        # new_stu_id = input('ID: ')
        new_student = Student(new_stu_fname, new_stu_lname)
        print('New Student Created')
    elif option == 3:
        # Add new grade to student
        stu_fname = input('Firstname: ')
        stu_lname = input('Lastname: ')
        grade = input('Grade to add: ')
        if new_stu_fname == stu_fname and new_stu_lname == new_stu_lname:
            student.add_grade(grade)                  #  **** how do I access a student who isn't stored anywhere?

    elif option == 4:
        # Add student to classroom
        add_student_to_classroom
        pass
    elif option == 5:
        # Remove student from classroom
        pass
    elif option == 6:
        # Print grade averages for classroom
        pass
    elif option == 7:
        # Print total average for classroom
        pass













# Tests needed:
#  if room ID does not meet criteria
#  if class max size not int
#  if add new stu not Y/N
