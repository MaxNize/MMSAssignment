class Mail:
    def __init__(self, topic, to, sender, bcc, cc, content, attachmentsPath) -> None:
        self.topic = topic
        self.to = to
        self.sender = sender
        self.bcc = bcc
        self.cc = cc
        self.content = content
        self.attachmentsPath = attachmentsPath