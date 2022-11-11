# Пример композиции:
class Salary:

    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return self.pay * 12


class Employee:

    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.salary = Salary(self.pay)

    def annual_salary(self):
        return f'Total: {str(self.salary.get_total() + self.bonus)}'


employee = Employee(100, 10)
print(employee.annual_salary())


# Пример агрегации:
class Bill:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return self.pay * 12


class Stranger:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_bill(self):
        return f'Total: {str(self.pay.get_total() + self.bonus)}'


bill = Bill(100)
stranger = Stranger(bill, 10)
print(stranger.annual_bill())
    