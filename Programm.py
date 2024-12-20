from ContactManagmentSystem import ContactManagementSystem
from FolderManagementSystem import FolderManagementSystem
from MailManagementSystem import MailManagementSystem
from UserManagementSystem import UserManagementSystem


class Programm:
    def __init__(self):
        self.UserManager = UserManagementSystem()
        self.MailManager = MailManagementSystem()
        self.FolderManager = FolderManagementSystem()
        self.ContactManager = ContactManagementSystem()
        
        self.UserManager.FolderManager = self.FolderManager
        self.FolderManager.MailManager = self.MailManager
        self.MailManager.FolderManager = self.FolderManager
        self.MailManager.UserManager = self.UserManager
        self.UserManager.ContactsManager = self.ContactManager

    def mainloop(self):
        self.UserManager.mainloop()