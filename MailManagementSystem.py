#This file is used to manage all the Mails that a User has revicved
from System import System
import datetime #provides classes for working with dates and times

class MailManagementSystem(System):
    def __init__(self):
        super().__init__()
        self.title = "MAIL"
#Display of all the mainfunctions 
        self.baseQuestion = '''
What do you want to do?
0: Close Mail
1: Delete Mail from Folder
2: Move to different Folder
3: Answer
4: Forward
'''
        self.FolderManager = False
        self.UserManager = False
#Mainfunction 1 allows the user to delete a selected  mail 
    def deleteMailQ(self):
        print("Do you really want to delete this Mail?")
        if (self.checkSafetyQuestion(input("(y/n) "))):
            self.deleteMail()

    def deleteMail(self):
        self.FolderManager.active.mails.remove(self.active)
        self.active = False
        self.running = False

#Mainfunction 2 allows the user to move a selected mail to antohter folder
    def moveMail(self, destination):
        if (destination == "CANCEL"):
            return True
        if (self.UserManager.active.checkForExistingFolder(destination)):
            self.UserManager.active.getFolder(destination).mails.append(self.active)
            self.deleteMail()
            print("Mail moved") 
            return True
        print("Folder does not exist")
        return False

    def moveMailQ(self):
        worked = False
        while (not worked):
            destination = input("Where do you want to move the Mail to? (CANCEL to cancel) ")
            worked = self.moveMail(destination)

#Mainfunction 3 allows the user to answer a mail they received
    def answerMail(self, content, attachmentsPath, time):
        subject = "AW: " + self.active.subject
        content = content + "\n Original Message: " + self.active.content
        attachmentsPath = self.active.attachmentsPath + attachmentsPath
        self.UserManager.active.sendMail(subject, self.active.sender, self.UserManager.active.mail, self.active.bcc, self.active.cc, content, attachmentsPath, time)


    def answerMailQ(self):
        content = input("Enter your answer (Dont hit enter unless your finished. For linebreaks use \\n): ")
        attachmentsPath = input("Enter filepath to your attachement in the attachements folder (PATH or leave blank): ")
        time = datetime.datetime.now()
        time = time.strftime("%Y-%m-%d %H:%M:%S")
        safety = input("Do you want to send the message? (y/n) ")
        if(self.checkSafetyQuestion(safety)):
            self.answerMail(content, attachmentsPath, time)
            print("Mail sent!")
            return
        print("Canceled")
#
    def updateBasedOnActivity(self):
        self.updadteBaseQuestion()
        self.updateTitle()

    def updadteBaseQuestion(self):
        self.baseQuestion = self.active.__str__()

        self.baseQuestion = self.baseQuestion + '''
What do you want to do?
0: Close mail
1: Delete mail from folder
2: Move to different folder
3: Answer
4: Forward
'''

    def updateTitle(self):
        if (not self.active):
            self.title = "MAIL : No Mail opened"
            return
        self.title = "MAIL : " + self.active.subject

    def initing(self):
        self.updateBasedOnActivity()
    #here are the switch case statments to execute the mainfunctions of this file

    def specificQuestionnaire(self, answer):
        match answer:
            case 1:
                self.deleteMailQ()
            case 2:
                self.moveMailQ()
            case 3:
                self.answerMailQ()
            case 4:
                self.forwardQ()
