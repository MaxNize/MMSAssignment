#This file is used to manage the various folders themselves 
from Abstracts.System import System

class FolderManagementSystem(System):
    def __init__(self):
        super().__init__()
#Overview of the data in a specific folder
        self.title = "Folder : No Folder open"
        self.baseQuestion = '''
What do you want to do?
0: Close Folder
No Mails in this Folder
'''
        self.MailManager = False
        self.UserManager = False

        self.updateBasedOnActivity()

    def updateTitle(self):
        if (not self.active):
            self.title = "Folder : No Folder open"
            return
        self.title = "Folder : " + self.active.name

    def updateBaseQuestion(self):
        if (not self.active or len(self.active.mails) == 0 ):
            self.baseQuestion = '''
What do you want to do?
0: Close Folder
1: delete Folder
No Mails in this Folder
'''
            return
        self.baseQuestion = '''
What do you want to do?
0: Close Folder
1: delete Folder
'''
        j = 2
        for i in self.active.mails:
            self.baseQuestion = self.baseQuestion+ str(j) + ": " + i.subject +  "\n"
            j += 1
#Mainfunction 1  deletes a folder
    def deleteFolder(self):
        if (len(self.UserManager.active.folders) > 1):
            self.UserManager.active.folders.remove(self.active)
            if (self.UserManager.active.inbox == self.active.name):
                self.UserManager.active.inbox = self.UserManager.active.folders[0].name
            if (self.UserManager.active.outbox == self.active.name):
                self.UserManager.active.outbox = self.UserManager.active.folders[0].name  
            if (self.UserManager.active.trash == self.active.name):
                self.UserManager.active.trash = self.UserManager.active.folders[0].name 

            print("Folder deleted and if needed folder settings changed to first folder")
            self.running = False
            return
        print("You need at least one folder")

    def deleteFolderQ(self):
        safety = input("Do you really want to delete the folder (All Mails in folder will also be deleted)? (y/n) ")
        if (self.checkSafetyQuestion(safety)):
            self.deleteFolder()
            print("Folder deleted")
            return
        print("Canceled")

    def deleteFolder(self):
        if (len(self.UserManager.active.folders) > 1):
            self.UserManager.active.folders.remove(self.active)
            if (self.UserManager.active.inbox == self.active.name):
                self.UserManager.active.inbox = self.UserManager.active.folders[0].name
            if (self.UserManager.active.outbox == self.active.name):
                self.UserManager.active.outbox = self.UserManager.active.folders[0].name  
            if (self.UserManager.active.trash == self.active.name):
                self.UserManager.active.trash = self.UserManager.active.folders[0].name 

            print("Folder deleted and if needed folder settings changed to first folder")
            self.running = False
            return
        print("You need at least one folder")

    def deleteFolderQ(self):
        safety = input("Do you really want to delete the folder (All Mails in folder will also be deleted)? (y/n) ")
        if (self.checkSafetyQuestion(safety)):
            self.deleteFolder()
            print("Folder deleted")
            return
        print("Canceled")

    def updateBasedOnActivity(self):
        self.updateBaseQuestion()
        self.updateTitle()

    def activateMailManager(self, mail):
        self.MailManager.active = mail
        self.MailManager.mainloop()

    def initing(self):
        self.updateBasedOnActivity()

    def specificQuestionnaire(self, answer):
        if (answer == 1):
            self.deleteFolderQ()
            return
        self.activateMailManager(self.active.mails[answer - 2])