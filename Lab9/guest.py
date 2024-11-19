from abc import ABC, abstractmethod

class Guest(ABC):
    @abstractmethod
    def guest_company(self, company):
        pass

    @abstractmethod
    def guest_section(self, section):
        pass

class SalaryReportGuest(Guest):
    def guest_company(self, company):
        print(f"Зарплатний звіт компанії: {company.get_name()}")

    def guest_section(self, section):
        print(f"Зарплатний звіт відділу: {section.get_name()}")