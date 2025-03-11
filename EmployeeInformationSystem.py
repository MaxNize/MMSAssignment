from Employee import Employee
from System import System

class EmployeeInformationSystem(System):
    def __init__(self, lastId):
        super().__init__()
        #These are System specific vars
        self.title = "Employee Information System"
        self.baseQuestion = '''
What do you want to do?
0: return to menu
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

    def printEmployeeQ(self, mode):
        self.TEXTheading("PRINT EMPLOYEE")
        match mode:
            case "all":
                for i in self.employees:
                    print(i)
            case "edit":
                for i in self.employees:
                    print(i)
                id = self.safeQuestion("Which employee do you want to edit? ", "int")
                for i in self.employees:
                    if i.id == id:
                        i.name = input("Name your Employee: ")
                        i.birthdate = self.safeQuestion("What's the birthdate of your Employee?: ", "string")
                        i.mail = self.safeQuestion("What's the mail of your Employee?: ", "mail")
                        i.role = input("What's the role of your Employee?: ")
                        i.hoursType = self.safeQuestion("What's the hoursType of your Employee?: ", "hourType")
                        i.baseSalary = self.safeQuestion("What's the baseSalary of your Employee?: ", "float")
                        i.comissionRate = self.safeQuestion("What's the comissionRate of your Employee?: ", "decimalPercentage")
                        print("Employee was edited")
                        return
                    
                print("No Employee with that ID was found!")
            case "delete":
                for i in self.employees:
                    print(i)
                id = self.safeQuestion("Which employee do you want to delete? ", "int")
                for i in self.employees:
                    if i.id == id:
                        self.employees.remove(i)
                        print("Employee was deleted")
                        return
                print("No Employee with that ID was found!")



    def specificQuestionnaire(self, answer):
        match answer:
            case 1:
                self.addNewEmployeeQ()
            case 2:
                self.printEmployeeQ("edit")
            case 3:
                self.printEmployeeQ("all")
            case 4:
                self.printEmployeeQ("delete")