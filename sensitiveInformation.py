# Create a class to represent a patient of a doctor's office. The Patient class will accept the following information during initialization:

# Social security number
# Date of birth
# Health insurance account number
# First name
# Last name
# Address

class Patient:

    def __init__(self, first_name, last_name, address, date_of_birth, social_security_number, health_insurance_account_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address
        self.__date_of_birth = date_of_birth
        self.__health_insurance_account_number = health_insurance_account_number
        self.__social_security_number = social_security_number

    # The first three properties should be read-only.
    @property
    def social_security_number(self):
        return self.__social_security_number
        
    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @property
    def health_insurance_account_number(self):
        return self.__health_insurance_account_number
      
    # First name and last name should not be exposed as properties at all, but instead expose a calculated property of full_name.
    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    # Address should have a getter and setter.
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        if type(address) is str:
            self.__address = address
        else:
            raise TypeError("Please enter a proper address.")
    
    def __str__(self):
        return f"{self.full_name} was born on {self.date_of_birth}. Her social security number is {self.social_security_number}, her insurance number is {self.health_insurance_account_number}, and her address is {self.address}."

Caroline = Patient("Caroline", "Brownlee", "104 Doral Ln", "Sept. 2, 1978", "555-555-5555", "IW55555")

print(Caroline)
