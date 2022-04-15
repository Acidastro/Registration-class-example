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
            raise TypeError("Пароль должен быть строкой")
        if not 4 < len(value) < 12:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not Registration.is_include_digit(value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not Registration.is_include_all_register(value):
            raise ValueError('Пароль должен содержать хотя бы 2 заглавные буквы')
        if Registration.is_include_only_latin(value):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        if Registration.check_password_dictionary(value):
            raise ValueError('Ваш пароль содержится в списке самых легких')
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
        count = 0
        for upp in ascii_uppercase:
            if upp in n:
                count += 1
                if count == 2:
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
