from guestable import Guestable

class Section(Guestable):
    def __init__(self, name, worker):
        self.name = name
        self.worker = worker

    def get_name(self):
        return self.name

    def get_employees(self):
        return self.worker

    def accept(self, guest):
        guest.guest_section(self)