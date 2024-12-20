import Folder

class User:
    def __init__(self, userName, firstName, lastName, mail, pw, default):
        self.userName = userName
        self.firstName = firstName
        self.lastName = lastName
        self.mail = mail
        self._pw = pw
        if (default):
            self.folders = [Folder.Folder("Inbox"), Folder.Folder("Sent"), Folder.Folder("Trash")]
        else:
            self.folders = []
        self.inbox = "Recieved"
        self.outbox = "Sent"
        self.trash = "Trash" 

    def sendMail(self, topic, to, sender, bcc, cc, content, attachmentsPath):
        for i in self.folders:
            if (i.name == self.outbox):
                i.createMail(topic, to, sender, bcc, cc, content, attachmentsPath)
            
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
        return pw == self._pw
    
    def getPw(self):
        return self._pw