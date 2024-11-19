from guestable import Guestable

class Company(Guestable):
    def __init__(self, name, section):
        self.name = name
        self.section = section

    def get_name(self):
        return self.name

    def get_departments(self):
        return self.section

    def accept(self, guest):
        guest.guest_company(self)
        for section in self.section:
            section.accept(guest)