class Mail:
    def __init__(self, subject, to, sender, bcc, cc, content, attachmentsPath, timestamp) -> None:
        self.subject = subject
        self.to = to
        self.sender = sender
        self.bcc = bcc
        self.cc = cc
        self.content = content
        self.attachmentsPath = attachmentsPath
        self.timestamp = timestamp

    def __str__(self):
        return f'\n\n{self.subject}\nTo: {self.to}\nFrom: {self.sender}\nBCC: {self.bcc}\nCC: {self.cc}\n{self.content}\n{self.attachmentsPath}\n'