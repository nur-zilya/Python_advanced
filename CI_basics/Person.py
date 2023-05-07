import datetime


class Person:
    def __init__(self, name, year_of_birth, address=''):
      self.name = name
      self.yob = year_of_birth
      self.address = address

    def get_age(self):
        def get_age(self):
            now = datetime.datetime.now()
            if now.year > self.yob > 0:
                return abs(self.yob - now.year)
            else:
                raise ValueError

    def get_name(self):
           return self.name

    def set_name(self, name):
           self.name = name

    def set_address(self, address):
           self.address = address

    def get_address(self):
           return self.address

    def is_homeless(self):
        return self.address is None