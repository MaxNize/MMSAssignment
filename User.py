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

    def login(self, userName, pw):
        return userName == self.userName and pw == self._pw    