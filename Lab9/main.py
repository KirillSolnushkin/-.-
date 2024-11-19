from worker import Worker
from section import Section
from company import Company
from guest import SalaryReportGuest

def main():
    WorkerNumber1 = Worker("Перший", 21000)
    WorkerNumber2 = Worker("Другий", 15000)

    section = Section("Відділ розслаблення :D", [WorkerNumber1, WorkerNumber2])

    company = Company("Релакс-Балдіж Компані ;)", [section])

    salary_report_guest = SalaryReportGuest()

    company.accept(salary_report_guest)

    section.accept(salary_report_guest)

if __name__ == "__main__":
    main()