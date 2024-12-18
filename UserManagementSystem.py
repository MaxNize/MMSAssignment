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
        self.active = False
        self.TEXTenterUserName = "Please enter a Username: "
        self.TEXTenterYourPw = "Please enter your Password: "


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
'''

    def updateBasedOnActivity(self):
        self.updateBaseQuestion()
        self.updateTitle()

    def logout(self):
        self.active = False
        self.updateBasedOnActivity()

    def writeMail(self):
        pass

    def openFolder(self):
        pass

    def createUserQ(self):
        self.TEXTheading("CREATE USER")

        userName = input(self.TEXTenterUserName)
        firstName = input("Please enter a Firstname: ")
        lastName = input("Please enter a Lastname: ")
        mail = input("Please enter a Mail: ") 
        emailPattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(emailPattern, mail):
            print("Your email is valid")
        else:
            print("Unvalid email entered! Please try again.")
            self.createUserQ()
           
            
        pw = input("Please enter a Password: ")
        pwTest = input("Please enter your verify your password: ")
        if pwTest == pw:
            self.createUser(userName, firstName, lastName, mail, pw)
        else:
            print("The entered passwords do not match! Please try again.")
            self.createUserQ()

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
        self.users.append(User(userName, firstName, lastName, mail, pw))

    def deleteUser(self, userName):
        try:
            self.users.remove(self.getUser(userName))
            return True
        except:
            return False

    def specificQuestionnaire(self, answer):
        if (not self.active):
            match answer:
                case 1:
                    print(1)
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

        self.updateBasedOnActivity()