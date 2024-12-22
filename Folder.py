import Mail

class Folder:
    def __init__(self, name) -> None:
        self.name = name
        self.mails = []

    def createMail(self, subject, to, sender, bcc, cc, content, attachmentsPath, timestamp):
        self.mails.append(Mail.Mail(subject, to, sender, bcc, cc, content, attachmentsPath, timestamp))

    def deleteMail(self, mailIndex):
        if (mailIndex < len(self.mails)):
            del self.mails[mailIndex]

    def getMailBySubject(self, subject):
        for i in self.mails:
            if (i.subject == subject):
                return i
        return None