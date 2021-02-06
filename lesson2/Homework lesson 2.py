class Employee(object):

    def __init__(self, name, email, zp_one_day):
        self.name = name
        self.email = email
        self.zp_one_day = zp_one_day

    def work(self):
        return 'I come to the office.'

    def check_salary(self, all_day):
        self.all_day = all_day
        return 'General zp = {}'.format(self.zp_one_day * self.all_day)


class Recruiter(Employee):
    position = 'Recruiter'

    def work(self):
        super().work()
        return 'I come to the office and start to hiring.'

    def __str__(self):
        return 'Должность: {}, Имя: {}'.format(self.position, self.name)



class Programmer(Employee):
    position = 'Programmer'

    def work(self):
        super().work()
        return 'I come to the office and start to coding.'

    def __str__(self):
        return 'Должность: {}, Имя: {}'.format(self.position, self.name)

Alex = Employee('Alex', 'alex228@gmail.com', 420)
print(Alex.zp_one_day)
print(Alex.work())
print(Alex.check_salary(365))

Angelica = Recruiter('Angelica', 'hotangelica@gmail.com', 500)
print(Angelica)
print(Angelica.work())

Bob = Programmer('Bob', 'marley@gmail.com', 1000)
print(Bob)
print(Bob.work())



