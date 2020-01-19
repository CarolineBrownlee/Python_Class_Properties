# Define a Python class named Student. This class will have 5 properties.

# First name (string)
# Last name (string)
# Age (integer)
# Cohort number (integer)
# Full name (read-only string)
# Define getters for all properties.
# Define a setter for all but the read only property.
# Ensure that only the appropriate value can be assigned to each.
# The full name property should return first name and last name separated by a space. It's value cannot be set.

class Student:
    
    # Define getters for all properties.
    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return "none"

    @property
    def last_name(self):
            try:
                return self.__last_name
            except AttributeError:
                return "none"
    @property        
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0
    @property        
    def cohort(self):
        try:
            return self.__cohort
        except AttributeError:
            return 0

    @property
    def full_name(self):
        try:
            return self.__full_name
        except AttributeError:
            return f"{self.first_name} {self.last_name}"

    # Define a setter for all but the read only property.
    @first_name.setter 
    def first_name(self, first_name):
        if type(first_name) is str:
            self.__first_name = first_name
        else:
            raise TypeError("Please enter a string value.")

    @last_name.setter
    def last_name(self, last_name):
        if type(last_name) is str:
            self.__last_name = last_name
        else:
            raise TypeError("Please enter a string value.")

    @age.setter
    def age(self, age):
        if type(age) is int:
            self.__age = age
        else:
            raise TypeError("Please enter an integer.")

    @cohort.setter
    def cohort(self, cohort):
        if type(cohort) is int:
            self.__cohort = cohort
        else:
            raise TypeError("Please enter an integer.")

    def __str__(self):
        return f"{self.full_name}"

# Ensure that only the appropriate value can be assigned to each.

Caroline = Student()
print(Caroline.first_name)
Caroline.first_name = "Caroline"
print(Caroline.first_name)
Caroline.age = 41
print(Caroline.age)
Caroline.last_name = "Brownlee"
print(Caroline.full_name)

print(Caroline)









