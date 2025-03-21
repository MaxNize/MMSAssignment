#This file contains the User class its attributes and functions   
import Models.Folder as Folder #is needed to know which flders and mails the user has 

class User:
    def __init__(self, userName, firstName, lastName, mail, pw, default):
        self.userName = userName
        self.firstName = firstName
        self.lastName = lastName
        self.mail = mail
        self.__pw = pw
        if (default):
            self.folders = [Folder.Folder("Inbox"), Folder.Folder("Sent"), Folder.Folder("Trash")]
        else:
            self.folders = []
        self.contacts = []
        self.inbox = "Recieved"
        self.outbox = "Sent"
        self.trash = "Trash" 

    def sendMail(self, subject, to, sender, bcc, cc, content, attachmentsPath, timestamp):
        for i in self.folders:
            if (i.name == self.outbox):
                i.createMail(subject, to, sender, bcc, cc, content, attachmentsPath, timestamp)

 # getter checking methodes          
    def getFolders(self):
        out = []
        for i in self.folders:
            out.append(i.name)
        return out
    
    def getFoldersForSave(self):
        out = ""
        for i in self.folders:
            out += i.name + ","
        return out[:-1]
    
    def checkForExistingFolder(self, folderName):
        for i in self.folders:
            if (i.name == folderName):
                return True
        return False
    
    def getFolder(self, folderName):
        for i in self.folders:
            if (i.name == folderName):
                return i
        return None
    
    def getMailsOfFolder(self, folderName):
        for i in self.folders:
            return i.mails
        
    def checkPw(self, pw):
        return pw == self.__pw
    
    def getPw(self):
        return self.__pw