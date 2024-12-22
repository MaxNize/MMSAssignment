from Folder import Folder
from System import System
from User import User
import re

class UserManagementSystem(System):
    def __init__(self):
        super().__init__()
        #These are System specific vars
        self.title = "MENU : No User logged in"
        self.baseQuestion = '''
What do you want to do?
0: STOP
1: create a new User
2: log into a User
3: delete a User
'''
        self.users = []
        self.FolderManager = False
        self.ContactsManager = False


    def checkForExistingUsername(self, userName):
        for i in self.users:
            if (i.userName == userName):
                return True
        return False
    
    def getUser(self, userName):
        for i in self.users:
            if (i.userName == userName):
                return i
        return None

    def TEXTnoUserWithUserNameAvailable(self, userName):
        return "No User with Username " + userName + " available!"

    def updateTitle(self):
        if (not self.active):
            self.title = "MENU : No User logged in"
            return
        self.title = "MENU : " + self.active.userName

    def updateBaseQuestion(self):
        if (not self.active):
            self.baseQuestion = '''
What do you want to do?
0: STOP
1: create a new User
2: log into a User
3: delete a User
'''
            return
        self.baseQuestion = '''
What do you want to do?
0: STOP
1: Logout
2: Write an Email
3: Open Folder
4: Contacts
'''

    def updateBasedOnActivity(self):
        self.updateBaseQuestion()
        self.updateTitle()

    def logout(self):
        self.active = False

    def writeMail(self):
        self.TEXTheading("WRITE MAIL")

        subject = input("Enter subject: ")
        to = input("Enter Receiver: ")
        if (self.checkForMailpattern(to)):
            bcc = input("Enter Bcc (or leave blank): ")
            cc = input("Enter Cc (or leave blank): ")
            content = input("Enter your mail (Dont hit enter unless your finished. For linebreaks use \\n): ")
            attachmentsPath = input("Enter filepath to your attachement in the attachements folder (PATH or leave blank): ")

            safety = input("Do you want to send the message? (y/n) ")
            if(self.checkSafetyQuestion(safety)):
                self.active.sendMail(subject, to, self.active.mail, bcc, cc, content, attachmentsPath)
                print("The Mail has been added to your Outbox!")
        else:
            print("That's not an email!")
            self.writeMail()

    def openFolder(self):
        success = False
        while (not success):
            for i in self.active.folders:
                print(i.name)
            folderName = input("Which Folder do you want to open? ")
            if (self.active.checkForExistingFolder(folderName)):
                self.FolderManager.active = self.active.getFolder(folderName)
                self.FolderManager.mainloop()
                success = True
            else:
                print("No Folder with that name available!")

    def createUserQ(self):
        self.TEXTheading("CREATE USER")
        
        while True:
             userName = input(self.TEXTenterUserName)
             firstName = input("Please enter a firstname: ")
             lastName = input("Please enter a lastname: ")
             mail = input("Please enter a mail: ") 
             if not self.checkForMailpattern(mail):
                 print("Invalid mail entered! Please try again.")
                 continue
             print("Your mail is valid")
             pw = input("Please enter a Password: ")
             pwTest = input("Please enter your verify your password: ")
             if pwTest != pw:
                 print("The entered passwords do not match! Please try again.")
                 continue
             self.createUser(userName, firstName, lastName, mail, pw)
             print("User was successfully created!")
             break
            
            

    def loginQ(self):
        self.TEXTheading("LOGIN")

        userName = input(self.TEXTenterUserName)
        if (self.checkForExistingUsername(userName)):
            pw = input(self.TEXTenterYourPw)
            user = self.getUser(userName)
            if (self.login(user, pw)):
                print("your now Logged in, ", userName,"!")
                return
        print(self.TEXTnoUserWithUserNameAvailable(userName))

    def deleteUserQ(self):
        self.TEXTheading("DELETING USER")

        userName = input(self.TEXTenterUserName)
        if (self.checkForExistingUsername(userName)):
            print("ARE YOU SURE ABOUT THAT?")
            print("THIS WILL DELETE ALL YOUR DATA PERMANANTLY")
            answer = input("y/n ")
            if (self.checkSafetyQuestion(answer)):
                pw = input(self.TEXTenterYourPw)
                user = self.getUser(userName)
                if (user.checkPw(pw)):
                    self.deleteUser(userName)
                    print("Successfully deleted User ", userName)
                    return
                print("Wrong Password!")
                return
        print(self.TEXTnoUserWithUserNameAvailable(userName))

    def login(self, user, pw):
        if (user.checkPw(pw)):
            self.active = user
            return True
        return False

    def createUser(self, userName, firstName, lastName, mail, pw):
        self.users.append(User(userName, firstName, lastName, mail, pw, True))

    def createUserSetup(self, userName, firstName, lastName, mail, pw, folders, inbox, outbox, trash):
        user = User(userName, firstName, lastName, mail, pw, False)
        folderNames = folders.split(",")
        for i in folderNames:
            user.folders.append(Folder(i))
        user.inbox = inbox
        user.outbox = outbox
        user.trash = trash
        self.users.append(user)

    def deleteUser(self, userName):
        try:
            self.users.remove(self.getUser(userName))
            return True
        except:
            return False
    
    def contacts(self):
        self.ContactsManager.mainloop()
        
    def initing(self):
        self.updateBasedOnActivity()

    def specificQuestionnaire(self, answer):
        if (not self.active):
            match answer:
                case 1:
                    self.createUserQ()
                case 2:
                    self.loginQ()
                case 3:
                    self.deleteUserQ()
        else:    
            match answer:
                case 1:
                    self.logout()
                case 2:
                    self.writeMail()
                case 3:
                    self.openFolder()
                case 4:
                    self.contacts() 