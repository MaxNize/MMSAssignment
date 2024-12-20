from System import System

class FolderManagementSystem(System):
    def __init__(self):
        super().__init__()
        self.title = "Folder : No Folder open"
        self.baseQuestion = '''
What do you want to do?
0: Close Folder
No Mails in this Folder
'''
        self.MailManager = False

        self.updateBasedOnActivity()

    def updateTitle(self):
        if (not self.active):
            self.title = "Folder : No Folder open"
            return
        self.title = "Folder : " + self.active.name

    def updateBaseQuestion(self):
        if (not self.active or len(self.active.mails) == 0 ):
            self.baseQuestion = '''
What do you want to do?
0: Close Folder
No Mails in this Folder
'''
            return
        self.baseQuestion = '''
What do you want to do?
0: Close Folder
'''
        j = 1
        for i in self.active.mails:
            self.baseQuestion = self.baseQuestion+ str(j) + ": " + i.topic + "\n"
            j += 1

    def updateBasedOnActivity(self):
        self.updateBaseQuestion()
        self.updateTitle()

    def activateMailManager(self, mail):
        self.MailManager.active = mail
        self.MailManager.mainloop()

    def initing(self):
        self.updateBasedOnActivity()

    def specificQuestionnaire(self, answer):
        self.activateMailManager(self.active.mails[answer - 1])