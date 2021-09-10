# Provide code that:
# A. Creates objects and shows the functionality.
# B. Asks for user input to:
#     - Add a new student   *Cr.1
#     - Add a new grade to a student   *Cr.2
#     - Add a student to a classroom    *Cr.3
#     - Remove a student from the classroom    *Cr.4
#     - Print all grade averages for a classroom    *Cr.5
#     - Print the total average for a classroom     *Cr.6

from classroom import Classroom
from student import Student


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



# initialise classroom anchor
classroom = None


# set up loop for options menu          - however everything only exists within this loop ?!
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
        print(f'New Classroom Created: {room_id}')
    elif option == 2:
        # Create new student                *** but where is this 'stored' to be accessed if not in a register?
        new_student_fname = input('Firstname: ')
        new_student_lname = input('Lastname: ')
        # new_student_id = input('ID: ')
        new_student = Student(new_student_fname, new_student_lname)
        print(f'New Student Created: {new_student_fname} {new_student_lname}')
    elif option == 3:
        # Add new grade to student
        student_fname = input('Firstname: ')
        student_lname = input('Lastname: ')
        grade = input('Grade to add: ')
        student = Student(student_fname, student_lname)
        #  **** how do I access a student who isn't stored anywhere?
        for student in #school_list
            if student.first_name == student_fname and student.last_name == student_lname:
                student.add_grade(grade)
        print(f'New Grade: {grade}; added to {student_fname} {student_lname}')
    elif option == 4:
        # Add student to classroom
        classroom = input('Classroom you want to add to: ')
        student_fname = input('Student to add; First Name: ')
        student_lname = input('Student to add; Last Name: ')
        student = Student(student_fname, student_lname)
        classroom.add_student_to_classroom(student)
        print(f'{student_fname} {student_lname} added to classroom {classroom}')
    elif option == 5:
        # Remove student from classroom
        classroom = input('Classroom you want to add to: ')
        student_fname = input('Student to add; First Name: ')
        student_lname = input('Student to add; Last Name: ')
        student = Student(student_fname, student_lname)
        classroom.remove_student_from_classroom(student)
        print(f'{student_fname} {student_lname} removed from classroom {classroom}')
    elif option == 6:
        # Print grade averages for classroom
        classroom = input('Which classroom would you like the average grades for?: ')
        print(f'List of average grade for each student in {classroom}')
        print(classroom.get_students_average_grades())
    elif option == 7:
        # Print total average for classroom
        class_average = classroom.get_classroom_average_grade()
        print(f'Class {classroom} average grade: {class_average}')


# Tests needed:
#  if room ID does not meet criteria
#  if class max size not int
#  if add new stu not Y/N
