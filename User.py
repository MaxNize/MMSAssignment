import Kategory

class User:
    def __init__(self, userName, firstName, lastName, mail, pw):
        self.userName = userName
        self.firstName = firstName
        self.lastName = lastName
        self.mail = mail
        self._pw = pw
        self.kategories = [Kategory.Kategory("Inbox"), Kategory.Kategory("Sent"), Kategory.Kategory("Trash")]
        self.inbox = "Recieved"
        self.outbox = "Sent"
        self.trash = "Trash" 

    def sendMail(self, topic, to, sender, bcc, cc, content, attachmentsPath):
        print("DEBUG: User.sendMail")
        for i in self.kategories:
            if (i.name == self.outbox):
                i.createMail(topic, to, sender, bcc, cc, content, attachmentsPath)
            
    def getFolders(self):
        out = []
        for i in self.kategories:
            out.append(i.name)
        return out
    
    def getMailsOfKategory(self, kategoryName):
        for i in self.kategories:
            return i.mails
        
    def checkPw(self, pw):
        return pw == self._pw