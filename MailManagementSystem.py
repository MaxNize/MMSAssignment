import User

class MailManagementSystem:
    def __init__(self):
        self.TEXTdivider = "********************************"
        self.TEXTspacer = "\n\n\n\n\n\n\n\n\n\n"
        self.TEXTenterUserName = "Please enter a Username: "
        self.TEXTenterYourPw = "Please enter your Password: "
        self.users = []
        self.running = True
        self.active = False

    def TEXTnoUserWithUserNameAvailable(self, userName):
        return "No User with Username " + userName + " available!"

    def createUser(self):
        print(self.TEXTdivider)
        print("CREATE USER")
        print(self.TEXTdivider)
        userName = input(self.TEXTenterUserName)
        firstName = input("Please enter a Firstname: ")
        lastName = input("Please enter a Lastname: ")
        mail = input("Please enter a Mail: ")
        pw = input("Please enter a Password: ")
        self.users.append(User.User(userName, firstName, lastName, mail, pw))

    def deleteUser(self):
        print(self.TEXTdivider)
        print("DELETING USER")
        print(self.TEXTdivider)
        userName = input(self.TEXTenterUserName)
        if (self.checkForExistingUsername(userName)):
            print("ARE YOU SURE ABOUT THAT?")
            print("THIS WILL DELETE ALL YOUR DATA PERMANANTLY")
            answer = input("y/n")
            if (self.checkSafetyQuestion(answer)):
                pw = input(self.TEXTenterYourPw)
                for i in self.users:
                    if (i.userName == userName):
                        self.users.remove(i)
                        print("Successfully deleted User ", userName)
                        break
            else:
                print("CANCELED")
        else:
            print(self.TEXTnoUserWithUserNameAvailable(userName))

        

    def logIntoUser(self):
        print(self.TEXTdivider)
        print("LOGIN")
        print(self.TEXTdivider)
        userName = input(self.TEXTenterUserName)
        if (self.checkForExistingUsername(userName)):
            pw = input(self.TEXTenterYourPw)
            for i in self.users:
                if (i.userName == userName):
                    if(i.login(userName, pw)):
                        self.active = i
                        print("your now Logged in, ", userName,"!")
                        break
        else:
            print(self.TEXTnoUserWithUserNameAvailable(userName))

    def writeMail(self):
        print(self.TEXTdivider)
        print("Write Mail")
        print(self.TEXTdivider)

        topic = input("Enter Topic: ")
        to = input("Enter Reciever: ")
        bcc = input("Enter Bcc (or leave blank): ")
        cc = input("Enter Topic (or leave blank): ")
        content = input("Enter your mail (Dont hit enter unless your finished. For linebreaks use \\n): ")
        attachments = input("Enter filepath to your attachement in the attachements folder (PATH): ")

        safety = input("Do you want to send the message? (y/n)")
        if(self.checkSafetyQuestion(safety)):
            pass #left here lol

    def logout(self):
        self.active = False

    def printAvailableUsers(self):
        for i in self.users:
            print(i.userName)

    def checkForExistingUsername(self, userName):
        for i in self.users:
            if (i.userName == userName):
                return True
        return False
    
    def checkSafetyQuestion(self, input):
        if (input == "y" or input == "Y" or input == "yes" or input == "Yes"):
            return True
        return False

    def askForActionsNoLogin(self):
        print(self.TEXTdivider)
        print("MENU")
        print(self.TEXTdivider)

        print("What do you want to do?")
        print("0: STOP")
        print("1: create a new User")
        print("2: log into a User")
        print("3: delete a User")
        out = input("A: ")
        return out
    
    def askForActionsLogin(self):
        print(self.TEXTdivider)
        print("MENU")
        print(self.TEXTdivider)

        print("What do you want to do?")
        print("0: STOP")
        print("1: Logout")
        print("2: Write an Email")
        print("3: delete a User")
        out = input("A: ")
        return out

    def mainloop(self):
        while (self.running):
            print(self.TEXTspacer)
            print(self.TEXTdivider)
            if (not self.active):
                print("**Not logged into an account!**")
                q = self.askForActionsNoLogin()

                match q:
                    case "0":
                        self.running = False
                    case "1":
                        self.createUser()
                    case "2":
                        self.logIntoUser()
                    case "3":
                        self.deleteUser()
                    case _:
                        print("LOL")
            else:
                print("********User: ", self.active.userName, "********")
                q = self.askForActionsLogin()

                match q:
                    case "0":
                        self.running = False
                    case "1":
                        self.logout()
                    case "2":
                        self.writeMail()
                    case "3":
                        self.deleteUser()
                    case _:
                        print("LOL")

            
