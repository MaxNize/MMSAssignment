#This file contains the folder class and its attributes and its functions
import Mail #Mail needs to be imported to Manipulate them in the folder
class Folder:
    def __init__(self, name) -> None:
        self.name = name
        self.mails = []

#functions 
    def createMail(self, subject, to, sender, bcc, cc, content, attachmentsPath):
        self.mails.append(Mail.Mail(subject, to, sender, bcc, cc, content, attachmentsPath))

    def deleteMail(self, mailIndex):
        if (mailIndex < len(self.mails)):
            del self.mails[mailIndex]

    def getMailBySubject(self, subject):
        for i in self.mails:
            if (i.subject == subject):
                return i
        return None