class Mail:
    def __init__(self, topic, to, sender, bcc, cc, content, attachmentsPath) -> None:
        self.topic = topic
        self.to = to
        self.sender = sender
        self.bcc = bcc
        self.cc = cc
        self.content = content
        self.attachmentsPath = attachmentsPath

    def __str__(self):
        return f'\n\n{self.topic}\nTo: {self.to}\nFrom: {self.sender}\nBCC: {self.bcc}\nCC: {self.cc}\n{self.content}\n{self.attachmentsPath}\n'