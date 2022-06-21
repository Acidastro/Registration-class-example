from string import digits
from string import ascii_uppercase


class Registration:
    """
    The class creates a new user with a username and password.
    """

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @login.setter
    def login(self, value):
        if '@' not in value:
            raise ValueError("Login must include at least one ' @ '")
        elif '.' not in value:
            raise ValueError("Login must include at least one ' . '")
        else:
            self.__login = value

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Password must be a string")
        if not 4 < len(value) < 12:
            raise ValueError('Password must be longer than 4 and less than 12 characters')
        if not Registration.is_include_digit(value):
            raise ValueError('Password must contain at least one number')
        if not Registration.is_include_all_register(value):
            raise ValueError('Password must contain at least 2 capital letters')
        if Registration.is_include_only_latin(value):
            raise ValueError('The password must contain only the Latin alphabet')
        if Registration.check_password_dictionary(value):
            raise ValueError('Your password is listed as the easiest')
        self.__password = value

    # check for at least one digit
    @staticmethod
    def is_include_digit(n):
        for digit in digits:
            if digit in n:
                return True
        return False

    # checking for at least two uppercase characters
    @staticmethod
    def is_include_all_register(n):
    if len([x for x in filter(lambda x: x in ascii_uppercase, n)]) > 1:
        return True
    return False

    # Checking for ownership of only Latin characters
    @staticmethod
    def is_include_only_latin(n):
        for i in n:
            if not i.isdigit():
                if i.upper() not in ascii_uppercase:
                    return True
        return False

    # Check if it belongs to the list of easy passwords
    @staticmethod
    def check_password_dictionary(n):
        with open('easy_passwords.txt', 'r', encoding='utf-8') as file:
            for password in file:
                if n == password.strip():
                    return True
            return False
