import Mail

class Kategory:
    def __init__(self, name) -> None:
        self.name = name
        self.mails = []

    def createMail(self, topic, to, sender, bcc, cc, content, attachmentsPath):
        self.mails.append(Mail.Mail(topic, to, sender, bcc, cc, content, attachmentsPath))