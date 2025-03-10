import Employee
import System

class EmployeeInformationSystem(System):
    def __init__(self, lastId):
        super().__init__()
        #These are System specific vars
        self.title = "Employee Information System"
        self.baseQuestion = '''
What do you want to do?
0: STOP
1: add new Employee
2: edit Employee
3: print Employee
4: delete Employee
'''
        self.employees = []
        self.lastId = lastId

    def addNewEmployeeQ(self):
        self.TEXTheading("ADD EMPLOYEE")
        name = input("Name your Employee: ")
        birthdate = self.safeQuestion("What's the birthdate of your Employee?: ", "string")
        mail = self.safeQuestion("What's the mail of your Employee?: ", "mail")
        role = input("What's the role of your Employee?: ")
        hoursType = self.safeQuestion("What's the hoursType of your Employee?: ", "hourType")
        baseSalary = self.safeQuestion("What's the baseSalary of your Employee?: ", "float")
        comissionRate = self.safeQuestion("What's the comissionRate of your Employee?: ", "decimalPercentage")
        self.lastId += 1
        self.employees.append(Employee(self.lastId, name, birthdate, role, mail, hoursType, baseSalary, comissionRate))

    def specificQuestionnaire(self, answer):
        match answer:
            case 1:
                self.addNewEmployeeQ()
            case 2:
                self.editEmployeeQ()
            case 3:
                self.printEmployeeQ()
            case 4:
                self.deleteEmployeeQ()