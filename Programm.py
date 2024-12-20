import json
from FolderManagementSystem import FolderManagementSystem
from MailManagementSystem import MailManagementSystem
from UserManagementSystem import UserManagementSystem
from db import db


class Programm:
    def __init__(self):
        self.UserManager = UserManagementSystem()
        self.MailManager = MailManagementSystem()
        self.FolderManager = FolderManagementSystem()

        self.UserManager.FolderManager = self.FolderManager
        self.FolderManager.MailManager = self.MailManager
        self.MailManager.FolderManager = self.FolderManager
        self.MailManager.UserManager = self.UserManager
        
        self.setupUsers()
        self.setupMails()

    def mainloop(self):
        self.UserManager.mainloop()
        self.save()

    def save(self):
        dataUsers = []
        dataMails = []
        for i in self.UserManager.users:
            dataUsers.append({"userName": i.userName, "firstName": i.firstName, "lastName": i.lastName, "mail": i.mail, "pw": i.getPw(), "folders": i.getFoldersForSave(), "inbox": i.inbox, "outbox": i.outbox, "trash": i.trash})
            print("DEBUG: " , i.folders)
            for j in i.folders:
                for k in j.mails:
                    dataMails.append({"topic": k.topic, "to": k.to, "sender": k.sender, "bcc": k.bcc, "cc": k.cc, "content": k.content, "attachmentsPath": k.attachmentsPath, "folder": j.name, "userName": i.userName})

        db.deleteUsers()
        db.setUsers(dataUsers)
        db.deleteMails()
        db.setMails(dataMails)
            

    def setupUsers(self):
        data = db.getUsers()
        for i in data:
            self.UserManager.createUserSetup(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])

    def setupMails(self):
        data = db.getMails()
        for i in data:
            print(i[8])
            self.UserManager.getUser(i[9]).getFolder(i[8]).createMail(i[1], i[2], i[3], i[4], i[5], i[6], i[7])