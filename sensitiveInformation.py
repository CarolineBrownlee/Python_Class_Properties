# Create a class to represent a patient of a doctor's office. The Patient class will accept the following information during initialization:

# Social security number
# Date of birth
# Health insurance account number
# First name
# Last name
# Address


class Patient:

    # The first three properties should be read-only.
    @property
    def social_security_number(self):
        try:
            return self.__social_security_number
        except AttributeError:
            return f"{self.social_security_number}"

    @property
    def date_of_birth(self):
        try:
            return self.__date_of_birth
        except AttributeError:
            return f"{self.date_of_birth}"

    @property
    def health_insurance_account_number(self):
        try:
            return self.__health_insurance_account_number
        except AttributeError:
            return f"{self.social_security_number}"

    # First name and last name should not be exposed as properties at all, but instead expose a calculated property of full_name.
    def first_name(self):
        return f"{self.first_name} {self.last_name}"

    def last_name(self):
        return f"{self.first_name} {self.last_name}"

    # Address should have a getter and setter.
    @property
    def address(self):
        try: 
            return self.__address
        except AttributeError:
            return f"{self.address}"
    
    @address.setter
    def address(self, address):
        if type(address) is str:
            self.__address = address
        else:
            raise TypeError("Please enter a proper address.")
