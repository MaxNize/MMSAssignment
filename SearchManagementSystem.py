from System import System
from db import db

class SearchManagementSystem(System):
    def __init__(self):
        super().__init__()
        self.title = "SEARCH"
        self.baseQuestion = '''
What do you want to search?
0: Cancel
1: Search by sender
2: Search by subject
3: Search by attachment
'''
        self.active = False
        self.MailManager = False
        self.UserManager = False

    def searchBySender(self, senderString):
        matches = db.getMailsBySenderString("%"+senderString+"%", self.UserManager.active.userName)

        print("0: Cancel")

        j = 1
        for i in matches:
            print(str(j) + ": " + i[1])
            j += 1

        succes = False
        while (not succes):
            answer = self.safeQuestion("Which Mail do you want to open? ", "int")
            if (answer == 0):
                return
            if (answer > len(matches)):
                print("No such Mail")
                continue
            self.MailManager.active = self.UserManager.getUser(matches[answer-1][9]).getFolder(matches[answer-1][8]).getMailBySubject(matches[answer-1][1])
            self.MailManager.mainloop()
            succes = True

    def searchBySubject(self, subjectString):
        matches = db.getMailsBySubjectString("%"+subjectString+"%", self.UserManager.active.userName)

        print("0: Cancel")
        print("DBUG: ", matches)

        j = 1
        for i in matches:
            print(str(j) + ": " + i[1])
            j += 1

        succes = False
        while (not succes):
            answer = self.safeQuestion("Which Mail do you want to open? ", "int")
            if (answer == 0):
                return
            if (answer > len(matches)):
                print("No such Mail")
                continue
            self.MailManager.active = self.UserManager.getUser(matches[answer-1][9]).getFolder(matches[answer-1][8]).getMailBySubject(matches[answer-1][1])
            self.MailManager.mainloop()
            succes = True

    def searchByAttachment(self, attachmentString):
        matches = db.getMailsByAttachmentString("%"+attachmentString+"%", self.UserManager.active.userName)

        print("0: Cancel")

        j = 1
        for i in matches:
            print(str(j) + ": " + i[1])
            j += 1

        succes = False
        while (not succes):
            answer = self.safeQuestion("Which Mail do you want to open? ", "int")
            if (answer == 0):
                return
            if (answer > len(matches)):
                print("No such Mail")
                continue
            self.MailManager.active = self.UserManager.getUser(matches[answer-1][9]).getFolder(matches[answer-1][8]).getMailBySubject(matches[answer-1][1])
            self.MailManager.mainloop()
            succes
        



    def specificQuestionnaire(self, answer):
        match answer:
                case 1:
                    self.searchBySender(input("Enter the sender you want to search for: "))
                case 2:
                    self.searchBySubject(input("Enter the sender you want to search for: "))
                case 3:
                    self.searchByAttachment(input("Enter the sender you want to search for: "))
