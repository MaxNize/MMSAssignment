from Folder import Folder
from System import System
from User import User
import datetime


class UserManagementSystem(System):
    def __init__(self):
        super().__init__()
        #These are System specific vars
        self.title = "MENU : No User logged in"
        self.baseQuestion = '''
What do you want to do?
0: return to menu
1: create a new User
2: log into a User
3: delete a User
'''
        self.users = []
        self.FolderManager = False
        self.ContactsManager = False
        self.SearchManager = False


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
0: return to Menu
1: create a new User
2: log into a User
3: delete a User
'''
            return
#While logged into a user 
        self.baseQuestion = '''
What do you want to do?
0: STOP
1: Logout
2: Write an Email
3: Open Folder
4: Contacts
5: Setup in, out and trash Folder
6: Search for mails
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
            time = datetime.datetime.now()
            time = time.strftime("%Y-%m-%d %H:%M:%S")
            safety = input("Do you want to send the message? (y/n) ")
            if(self.checkSafetyQuestion(safety)):
                self.active.sendMail(subject, to, self.active.mail, bcc, cc, content, attachmentsPath, time)
                print("The Mail has been added to your Outbox!")
        else:
            print("That's not an email!")
            self.writeMail()

    def openFolder(self):
        success = False
        while (not success):
            for i in self.active.folders:
                print(i.name)
            folderName = input("Which Folder do you want to open or create(print: create)? ")
            if (folderName == "create"):
                name = input("Enter the name of the new Folder: ")
                if (self.active.checkForExistingFolder(name)):
                    print("Folder already exists!")
                    return
                self.active.folders.append(Folder(name))
                return
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
            if (self.checkForExistingUsername(userName)):
                print("Username already exists! Please try again.")
                continue
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
            answer = input("(y/n): ")
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

    def setupFoldersQ(self):
        self.TEXTheading("SETUP FOLDERS")

        for i in self.active.folders:
                print(i.name)

        inbox = input("Enter the name of your Inbox: ")
        if (not self.active.checkForExistingFolder(inbox)):
            print("No Folder available")
            return
        outbox = input("Enter the name of your Outbox: ")
        if (not self.active.checkForExistingFolder(outbox)):
            print("No Folder available")
            return
        trash = input("Enter the name of your Trash: ")
        if (not self.active.checkForExistingFolder(trash)):
            print("No Folder available")
            return
        
        self.setupFolders(inbox, outbox, trash)

    def setupFolders(self, inbox, outbox, trash):
        self.active.inbox = inbox
        self.active.outbox = outbox
        self.active.trash = trash

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

    def searchMails(self):
        self.SearchManager.mainloop()
            
    def deleteUser(self, userName):
        try:
            self.users.remove(self.getUser(userName))
            return True
        except:
            return False
    
    def contacts(self):
        self.ContactsManager.active = self.active
        self.ContactsManager.mainloop()
        
    def initing(self):
        self.updateBasedOnActivity()

#here are the switch case statments to execute the mainfunctions of this file
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
                case 5:
                    self.setupFoldersQ()
                case 6:
                    self.searchMails()