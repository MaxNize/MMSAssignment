from Employee import Employee
from HoursAndSales import HoursAndSales
from System import System
import logging

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
5: add hours and sales
6: edit hours and sales
7: print hours and sales
8: send payslip
'''
        self.employees = []
        self.lastId = lastId
        self.hoursSales = []

    @logging.logger
    def addNewEmployeeQ(self):
        self.TEXTheading("ADD EMPLOYEE")
        name = input("Name your Employee: ")
        birthdate = self.safeQuestion("What's the birthdate of your Employee?: ", "date")
        mail = self.safeQuestion("What's the mail of your Employee?: ", "mail")
        role = input("What's the role of your Employee?: ")
        hoursType = self.safeQuestion("What's the hoursType of your Employee?: ", "hourType")
        baseSalary = self.safeQuestion("What's the baseSalary of your Employee?: ", "float")
        comissionRate = self.safeQuestion("What's the comissionRate of your Employee?: ", "decimalPercentage")
        self.lastId += 1
        employee = Employee(self.lastId, name, birthdate, role, mail, hoursType, baseSalary, comissionRate)
        self.employees.append(employee)
        return "CREATE EMPLOYEE: " + employee.__str__()

    @logging.logger
    def printEmployeeQ(self, mode):
        self.TEXTheading("PRINT EMPLOYEE")
        match mode:
            case "all":
                for i in self.employees:
                    if i.name == None:
                        continue
                    print(i)
                return "READ ALL EMPLOYEES"
            case "edit":
                for i in self.employees:
                    if i.name == None:
                        continue
                    print(i)
                id = self.safeQuestion("Which employee do you want to edit? ", "int")
                for i in self.employees:
                    if i.id == id:
                        i.name = input("Name your Employee: ")
                        i.birthdate = self.safeQuestion("What's the birthdate of your Employee?: ", "date")
                        i.mail = self.safeQuestion("What's the mail of your Employee?: ", "mail")
                        i.role = input("What's the role of your Employee?: ")
                        i.hoursType = self.safeQuestion("What's the hoursType of your Employee?: ", "hourType")
                        i.baseSalary = self.safeQuestion("What's the baseSalary of your Employee?: ", "float")
                        i.comissionRate = self.safeQuestion("What's the comissionRate of your Employee?: ", "decimalPercentage")
                        print("Employee was edited")
                        return "EDIT EMPLOYEE TO: " + i.__str__()
                print("No Employee with that ID was found!")
                return "EDIT EMPLOYEE BUT GIVEN ID WAS NOT FOUND"
            case "delete":
                for i in self.employees:
                    print(i)
                id = self.safeQuestion("Which employee do you want to delete? ", "int")
                if self.checkSafetyQuestion(input("ARE YOU SURE? THIS WILL DELETE DATA PERMANANTLY (y/Y)")):
                    for i in self.employees:
                        if i.id == id:
                            i.name = None
                            i.birthdate = None
                            i.role = None
                            i.hoursType = None
                            i.baseSalary = None
                            i.comissionRate = None
                            i.mail = None
                            print("Employee was deleted")
                            return "DELETE EMPLOYEE WITH ID: ", i.id
                    print("No Employee with that ID was found!")
                    return "DELETE EMPLOYEE BUT GIVEN ID WAS NOT FOUND"
            case "addHoursSales":
                for i in self.employees:
                    if i.name == None:
                        continue
                    print(i)
                id = self.safeQuestion("For which Employee do you want to enter data?: ", "int")
                for i in self.employees:
                    if i.id == id:
                        date = self.safeQuestion("Enter a date: ", "date")
                        hours = self.safeQuestion("Enter hours worked: ", "float")
                        sales = self.safeQuestion("Enter sales: ", "float")
                        data = HoursAndSales(self.hoursSales[-1].id +1, id, date, sales, hours)
                        self.hoursSales.append(data)
                        print("Data was entered")
                        return "ENTER HOURS AND SALES FOR EMPLOYEE: " + data.__str__()
                print("No Employee with that ID was found!")
                return "ENTER HOURS AND SALES BUT GIVEN EMPLOYEE ID WAS NOT FOUND"
                
            case "editHoursSales":
                for i in self.hoursSales:
                    print(i)
                id = self.safeQuestion("Which Entry do you want to edit?: ", "int")
                for i in self.hoursSales:
                    if id == i.id:
                        i.hours = self.safeQuestion("Enter hours worked: ", "float")
                        i.sales = self.safeQuestion("Enter sales: ", "float")
                        print("Data was edited")
                        return "EDIT HOURS AND SALES FOR TO: " + i.__str__()
                print("No Entry with that ID was found!")
                return "EDIT HOURS AND SALES BUT GIVEN ID WAS NOT FOUND"
            
            case printHoursSales:
                for i in self.hoursSales:
                    print(i)




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
            case 5:
                self.printEmployeeQ("addHoursSales")
            case 6:
                self.printEmployeeQ("editHoursSales")
            case 7:
                self.printEmployeeQ("printHoursSales")
            case 8:
                self.printEmployeeQ("sendPayslip")