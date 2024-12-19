from FolderManagementSystem import FolderManagementSystem
from MailManagementSystem2 import MailManagementSystem
from UserManagementSystem import UserManagementSystem


class Programm:
    def __init__(self):
        self.UserManager = UserManagementSystem()
        self.MailManager = MailManagementSystem()
        self.FolderManager = FolderManagementSystem()

        self.UserManager.FolderManager = self.FolderManager
        self.FolderManager.MailManager = self.MailManager

    def mainloop(self):
        self.UserManager.mainloop()