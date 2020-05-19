import string
import random


class SetUpEmployee:

    def __init__(self):

        """ Collect Employee Details """

        self.Firstname = input('Enter Employee FirstName: ')
        self.Lastname = input('Enter Employee LastName: ')
        self.Email = input('Enter Employee Email: ')
        self._Password = self.generate_password()
        self.interact_with_employee()

    @property
    def password(self):

        """ Password Getter """
        return self._Password

    @password.setter
    def password(self, value):

        """ Passowrd Setter """

        if len(value) < 7:
            raise ValueError('Length of Password is Less than 7 characters')
        self._Password = value

    def generate_password(self):

        """ Generate Random Password for Employee """

        password = self.Firstname[:2] + self.Lastname[:2] + ''.join(random.choices(string.ascii_lowercase, k=5))
        return password

    def employee_generate_password(self):
        self.password = input('Enter Your Preferred Password: ')

    def display_employee_info(self):
        self.save_to_container()
        print(f'FirstName: {self.Firstname} \nFirstName : {self.Lastname}'
              f' \nEmail : {self.Email} \nPassowrd:{self.password}')

    def save_to_container(self):
        container_dict = {'firstname': self.Firstname, 'lastname': self.Lastname, 'email': self.Email,
                          'password': self.password}
        with open('Container.txt', 'a+') as file:
            file.write(str(container_dict))
            file.write('\n')

    def interact_with_employee(self):
        print(f'Your Password is {self.password}')
        employee_input = input('Are You Satisfied with Password: Yes (Y) or No (N): ')
        if employee_input.upper() in ['YES', 'Y']:
            self.display_employee_info()
        elif employee_input.upper() in ['NO', 'N']:
            while True:
                try:
                    self.employee_generate_password()
                    self.display_employee_info()
                    break
                except ValueError as e:
                    print(e)
                    continue
        else:
            self.interact_with_employee()


if __name__ == '__main__':
    SetUpEmployee()
