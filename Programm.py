from Contact import Contact
from ContactManagmentSystem import ContactManagementSystem
import json
from FolderManagementSystem import FolderManagementSystem
from MailManagementSystem import MailManagementSystem
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
        
        self.setupUsers()
        self.setupMails()
        self.setupContacts()

    def mainloop(self):
        self.UserManager.mainloop()
        self.save()

    def save(self):
        dataUsers = []
        dataMails = []
        dataContacts = []
        for i in self.UserManager.users:
            dataUsers.append({"userName": i.userName, "firstName": i.firstName, "lastName": i.lastName, "mail": i.mail, "pw": i.getPw(), "folders": i.getFoldersForSave(), "inbox": i.inbox, "outbox": i.outbox, "trash": i.trash})
            for j in i.folders:
                for k in j.mails:
                    dataMails.append({"subject": k.subject, "to": k.to, "sender": k.sender, "bcc": k.bcc, "cc": k.cc, "content": k.content, "attachmentsPath": k.attachmentsPath, "folder": j.name, "userName": i.userName, "timestamp": k.timestamp})
            for l in i.contacts:
                dataContacts.append({"name": l.name, "firstName": l.firstName, "lastName": l.lastName, "mail": l.mail, "userName": l.userName, "phone": l.phone})

        db.deleteUsers()
        db.setUsers(dataUsers)
        db.deleteMails()
        db.setMails(dataMails)
        db.deleteContacts()
        db.setContacts(dataContacts)
            

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