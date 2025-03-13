from Employee import Employee
from HoursAndSales import HoursAndSales
from System import System
import logging
from datetime import datetime
import FileHandling

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
8: send payslips
'''
        self.employees = []
        self.lastId = lastId
        self.hoursSales = []
        self.dateFormat = "%d.%m.%Y"
        self.UserManager = False

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
    def printEmployeeQ(self):
        self.TEXTheading("PRINT EMPLOYEE")
        for i in self.employees:
            if i.name == None:
                continue
            print(i)
        return "READ ALL EMPLOYEES"
                
            
    @logging.logger
    def editEmployee(self):
        self.TEXTheading("EDIT EMPLOYEE")
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
                
    @logging.logger
    def deleteEmployee(self):
        self.TEXTheading("DELETE EMPLOYEE")
        for i in self.employees:
            if i.name == None:
                continue
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
                    return "DELETE EMPLOYEE WITH ID: " + str(i.id)
            print("No Employee with that ID was found!")
            return "DELETE EMPLOYEE BUT GIVEN ID WAS NOT FOUND"
                
    @logging.logger
    def addHoursSales(self):
        self.TEXTheading("ENTER HOURS AND SALES")
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
                
    @logging.logger
    def editHoursSales(self):
        self.TEXTheading("Edit HOURS AND SALES")
        for i in self.hoursSales:
            if list(filter(lambda x: x.id == i.employeeId, self.employees))[0].name == None:
                continue
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


    @logging.logger
    def printHoursSales(self):
        self.TEXTheading("PRINT HOURS AND SALES")
        for i in self.hoursSales:
            print(i)
        return "PRINT ALL HOURS AND SALES"

    @logging.logger
    def sendPayslipQ(self):
        self.TEXTheading("SEND PAYSLIP")
        start = self.safeQuestion("Enter StartDate: ", "date")
        end = self.safeQuestion("Enter enddate: ", "date")
        startDate = datetime.strptime(start, self.dateFormat)
        endDate = datetime.strptime(end, self.dateFormat)

        availableData = []
        for i in self.hoursSales:
            for j in self.employees:
                if i.employeeId == j.id:
                    if j.name == None:
                        continue
                    availableData.append(i)

        dataInRange = list(filter(lambda date: startDate <= datetime.strptime(date.date, self.dateFormat) <= endDate, availableData))
        employeeIDs = set(map(lambda data: data.employeeId, dataInRange))
        dataSets = []
        for i in employeeIDs:
            dataSets.append(list(filter(lambda date: date.employeeId == i, dataInRange)))

        for i in dataSets:
            sortedData = sorted(i, key=lambda entry: datetime.strptime(entry.date, self.dateFormat))
            employee = list(filter(lambda employee: employee.id == i[0].employeeId, self.employees))

            self.sendPayslip(sortedData, employee)
        return "SEND PAYSLIPS FOR ENTRIES IN RANGE " + start + " - " + end

    @logging.logger
    def sendPayslip(self, data, employee):
        file = FileHandling.createPayslip(data, employee[0])
        self.mailPayslip(file, employee[0])

        return "CREATE PAYSLIP FOR EMPLOYEE " + employee[0].name
    
    @logging.logger
    def mailPayslip(self, file, employee):
        self.UserManager.login(self.UserManager.getUser("Accounting"), "company_Accounting")
        time = datetime.now()
        time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.UserManager.active.sendMail("Your Payslip", employee.mail, self.UserManager.active.mail, "", "", "Dear " + employee.name + ", \n with this mail we send you your payslip (attachments). \n kind regards, \n your accounting team", file, time)
        self.UserManager.logout()
        return "MAIL PAYSLIP TO EMPLOYEE " + employee.name




    def specificQuestionnaire(self, answer):
        match answer:
            case 1:
                self.addNewEmployeeQ()
            case 2:
                self.editEmployee()
            case 3:
                self.printEmployeeQ()
            case 4:
                self.deleteEmployee()
            case 5:
                self.addHoursSales()
            case 6:
                self.editHoursSales()
            case 7:
                self.printHoursSales()
            case 8:
                self.sendPayslipQ()