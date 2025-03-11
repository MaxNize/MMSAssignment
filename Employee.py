class Employee:
    def __init__(self, id, name, birthdate, role, mail, hoursType, baseSalary, comissionRate):
        self.id = id
        self.name = name
        self.birthdate = birthdate
        self.role = role
        self.mail = mail
        self.hoursType = hoursType
        self.baseSalary = baseSalary
        self.comissionRate = comissionRate

    def __str__(self):
        return f"{self.id}: {self.name}, {self.birthdate}, {self.role}, {self.mail}, {self.hoursType}, {self.baseSalary}, {self.comissionRate}"