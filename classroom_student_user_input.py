# Provide code that:
# A. Creates objects and shows the functionality.
# B. Asks for user input to:
#     - Add a new student
#     - Add a new grade to a student
#     - Add a student to a classroom
#     - Remove a student from the classroom
#     - Print all grade averages for a classroom
#     - Print the total average for a classroom

import class_classroom
import class_student


def create_new_classroom():
    # Create a new object from Class classroom with attributes for Class ID and Max class size.
    room_id = input('Insert new classroom ID, eg. room_01, room_02: ')
    max_room_size = input('Insert new classroom maximum size, eg 20, 25: ')
    class_classroom.Classroom(room_id, max_room_size)

student1 = class_student.Student("John", "Sheridan")
student2 = class_student.Student("Wolfgang", "Amadeus")

# class_classroom.Classroom.add_student('John', 'Sheridan')
# class_classroom.Classroom.add_student('Wolfgang', 'Amadeus')



# room_01 = class_classroom.Classroom("room_01", 25)
# room_02 = class_classroom.Classroom("room_02", 40)
