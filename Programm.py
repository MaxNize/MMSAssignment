from Contact import Contact
from ContactManagementSystem import ContactManagementSystem
import json
from Employee import Employee
from EmployeeInformationSystem import EmployeeInformationSystem
from FolderManagementSystem import FolderManagementSystem
from HoursAndSales import HoursAndSales
from MailManagementSystem import MailManagementSystem
from MenuSystem import MenuSystem
from SearchManagementSystem import SearchManagementSystem
from UserManagementSystem import UserManagementSystem
from db import db


class Programm:
    def __init__(self):
        self.UserManager = UserManagementSystem()
        self.MailManager = MailManagementSystem()
        self.FolderManager = FolderManagementSystem()
        self.ContactManager = ContactManagementSystem()
        self.SearchManager = SearchManagementSystem()
        self.EmployeeManager = EmployeeInformationSystem(db.getLastEmployeeID())
        
        self.UserManager.FolderManager = self.FolderManager
        self.FolderManager.MailManager = self.MailManager
        self.MailManager.FolderManager = self.FolderManager
        self.MailManager.UserManager = self.UserManager
        self.UserManager.ContactsManager = self.ContactManager
        self.ContactManager.UserManager = self.UserManager
        self.FolderManager.UserManager = self.UserManager
        self.UserManager.SearchManager = self.SearchManager
        self.SearchManager.MailManager = self.MailManager
        self.SearchManager.UserManager = self.UserManager
        self.EmployeeManager.UserManager = self.UserManager
        
        self.setupUsers()
        self.setupMails()
        self.setupContacts()
        self.setupEmployees()
        self.setupHoursAndSales()

        self.MenuManager = MenuSystem(self.UserManager, self.EmployeeManager)

    def mainloop(self):
        self.MenuManager.mainloop()
        self.save()

    def save(self):
        dataUsers = []
        dataMails = []
        dataContacts = []
        dataEmployees = []
        dataHoursAndSales = []
        for i in self.UserManager.users:
            dataUsers.append({"userName": i.userName, "firstName": i.firstName, "lastName": i.lastName, "mail": i.mail, "pw": i.getPw(), "folders": i.getFoldersForSave(), "inbox": i.inbox, "outbox": i.outbox, "trash": i.trash})
            for j in i.folders:
                for k in j.mails:
                    dataMails.append({"subject": k.subject, "to": k.to, "sender": k.sender, "bcc": k.bcc, "cc": k.cc, "content": k.content, "attachmentsPath": k.attachmentsPath, "folder": j.name, "userName": i.userName, "timestamp": k.timestamp})
            for l in i.contacts:
                dataContacts.append({"name": l.name, "firstName": l.firstName, "lastName": l.lastName, "mail": l.mail, "userName": l.userName, "phone": l.phone})

        for i in self.EmployeeManager.employees:
            dataEmployees.append({"id": i.id, "name": i.name, "birthdate": i.birthdate, "role": i.role, "mail": i.mail, "hoursType": i.hoursType, "baseSalary": i.baseSalary, "comissionRate": i.comissionRate})

        for i in self.EmployeeManager.hoursSales:
            dataHoursAndSales.append({"id": i.id, "employeeId": i.employeeId, "date": i.date, "sales": i.sales, "hoursWorked": i.hoursWorked})

        db.deleteUsers()
        db.setUsers(dataUsers)
        db.deleteMails()
        db.setMails(dataMails)
        db.deleteContacts()
        db.setContacts(dataContacts)
        db.deleteEmployees()
        db.setEmployees(dataEmployees)
        db.deleteHoursAndSales()
        db.setHoursAndSales(dataHoursAndSales)
            

    def setupUsers(self):
        data = db.getUsers()
        for i in data:
            self.UserManager.createUserSetup(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])

    def setupMails(self):
        data = db.getMails()
        for i in data:
            self.UserManager.getUser(i[9]).getFolder(i[8]).createMail(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[10])

    def setupContacts(self):
        data = db.getContacts()
        for i in data:
            self.UserManager.getUser(i[4]).contacts.append(Contact(i[0], i[1], i[2], i[3], i[4], i[5]))

    def setupEmployees(self):
        data = db.getEmployees()
        for i in data:
            self.EmployeeManager.employees.append(Employee(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))

    def setupHoursAndSales(self):
        data = db.getHoursAndSales()
        for i in data:
            self.EmployeeManager.hoursSales.append(HoursAndSales(i[0], i[1], i[2], i[3], i[4]))