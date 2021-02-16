class Employee(object):

    def __init__(self, name, email, zp_one_day):
        self.name = name
        self.email = email
        file = open('email.txt', 'a')
        with open('email.txt', 'r') as e:
            for i in e:
                if self.email in i:
                    raise ValueError("email exists")
        file.write(self.email + '\n')
        file.close()
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
        return '{}: {}'.format(self.position, self.name)


class Programmer(Employee):
    position = 'Programmer'

    def work(self):
        super().work()
        return 'I come to the office and start to coding.'

    def __str__(self):
        return '{}: {}'.format(self.position, self.name)


class Candidate:
    position = "Candidate"

    def __init__(self, full_name, email, technologies,
                 main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    def work(self):
        raise UnableToWorkException('I’m not hired yet, lol.')

    def __str__(self):
        return '{}: {}, {}, {}, {}, {}'.format(self.position, self.full_name, self.email,
                                               self.technologies, self.main_skill, self.main_skill_grade)


class Vacancy:
    position = "Vacancy"

    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level

    def __str__(self):
        return '{}: {}, {}, {}'.format(self.position, self.title, self.main_skill, self.main_skill_level)


class UnableToWorkException(Exception):
    pass

