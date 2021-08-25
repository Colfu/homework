class Student:
    """Create a class Student that keeps records of students
    
    param: first name (str)
    param: last name (str)
    param: graduation year (int) (if student graduated, otherwise leave empty)
    param: grades_list (list of int) (each grade an int between 1 and 100)
    param: address_list (list of str) [number, street, town_city, country, postcode]
    param: notes (list of str)
    """
    def __init__(self, first_name, last_name, graduation_year, grades_list, address_list, notes):
        # All the info connected to the student
        self.f_name = first_name
        self.l_name = last_name
        self.grad_year = graduation_year
        self.grades_list = grades_list
        self.address_list = address_list
        self.notes = notes

student1 = Student("John", "Sheridan", 2003, [34, 56, 89, 73, 67], ["42", "Locatia Drive", "Springfield", "Wales", "SA72 8OD" ], ["Maintains a good standard. Could focus more on the task at hand rather than planning ahead all the time."])
student2 = Student("Wolfgang", "Amadeus", 1770, [98, 87, 76, 77, 99], ["43", "Violin Street", "Vienna", "V1 QWERTY"], ["Excellent at improvising. Often forgets to take breats / sleep."])

if student1.f_name == 'John':
    print(True)