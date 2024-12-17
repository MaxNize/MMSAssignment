import User

class MailManagementSystem:
    def __init__(self):
        #These are for same texts everywhere
        self.TEXTdivider = "********************************"
        self.TEXTspacer = "\n\n\n\n\n\n\n\n\n\n"
        self.TEXTenterUserName = "Please enter a Username: "
        self.TEXTenterYourPw = "Please enter your Password: "
        #These are actual attributes. We need them :)
        self.users = []
        self.running = True
        self.active = False

    ########################################################################
    #This is only for Testing purposes
    def SETUPFORDEBUGGING(self):
        self.users.append(User.User("m", "m", "m", "m", "m"))
        self.active = self.users[0]
        self.active.sendMail("Hey", "to", self.active.mail, "", "", "Hey jo whatsup", "")

    ########################################################################
    #These are helper functions. They keep everything nice and clean
        #***********************************************************************
        #These are for Text Stuff. They are fun and save typing. Nothing too special :)
    def TEXTnoUserWithUserNameAvailable(self, userName):
        return "No User with Username " + userName + " available!"
    
    def TEXTheading(self, text):
        print(self.TEXTdivider)
        print(text)
        print(self.TEXTdivider)

        #***********************************************************************
        #These functions are functional. it is so cool that I just have to write one line instead of 5
    def getUser(self, userName):
        for i in self.users:
            if (i.userName == userName):
                return i
        return None
    
    def getFolderOfActive(self, folderName):
        for i in self.active.kategories:
            if (i.name == folderName):
                return i
        return None
    
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

    ########################################################################
    #These are the main functions that are called by the user. They should be small and clean. Call a helper function :)
    def createUser(self):
        self.TEXTheading("CREATE USER")

        userName = input(self.TEXTenterUserName)
        firstName = input("Please enter a Firstname: ")
        lastName = input("Please enter a Lastname: ")
        mail = input("Please enter a Mail: ")
        pw = input("Please enter a Password: ")
        self.users.append(User.User(userName, firstName, lastName, mail, pw))

    def deleteUser(self):
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
                    self.users.remove(user)
                    print("Successfully deleted User ", userName)
                    return
                print("Wrong Password!")
                return
        print(self.TEXTnoUserWithUserNameAvailable(userName))

    def logIntoUser(self):
        self.TEXTheading("LOGIN")

        userName = input(self.TEXTenterUserName)
        if (self.checkForExistingUsername(userName)):
            pw = input(self.TEXTenterYourPw)
            user = self.getUser(userName)
            if (user.checkPw(pw)):
                self.active = user
                print("your now Logged in, ", userName,"!")
                return
        print(self.TEXTnoUserWithUserNameAvailable(userName))

    def writeMail(self):
        self.TEXTheading("WRITE MAIL")

        topic = input("Enter Topic: ")
        to = input("Enter Reciever: ")
        bcc = input("Enter Bcc (or leave blank): ")
        cc = input("Enter Cc (or leave blank): ")
        content = input("Enter your mail (Dont hit enter unless your finished. For linebreaks use \\n): ")
        attachmentsPath = input("Enter filepath to your attachement in the attachements folder (PATH or leave blank): ")

        safety = input("Do you want to send the message? (y/n) ")
        if(self.checkSafetyQuestion(safety)):
            self.active.sendMail(topic, to, self.active.mail, bcc, cc, content, attachmentsPath)
            print("The Mail has been added to your Outbox!")

    def logout(self):
        self.active = False

    def selectFolder(self):
        self.TEXTheading("OPEN FOLDER")

        print("Your Folders: ")
        for i in self.active.kategories:
            print(i.name)

        folderName = input("Which Folder do you want to open? ")
        self.enterFolder(folderName)

    def enterFolder(self, folderName):
        self.TEXTheading(folderName+"- Folder")
        folder = self.getFolderOfActive(folderName)

        j = 0
        for i in folder.mails:
            print(j, ": ", i.topic)
            j+=1

        mailIndex = int(input("Which mail do you want to open?: "))
        print(folder.mails[mailIndex])

        self.askForMailOptions(folder, mailIndex)
                
    ########################################################################
    #Here is the Menuing done :). keep everything here
    def askForMailOptions(self, folder, mailIndex):
            print("Available Actions: ")
            print("0: delete Mail from folder")
            print("1: move to different folder")
            print("2: answer")
            print("3: forward")
            answer = int(input("A: "))

            self.reactForAnswersMailOptions(answer, folder, mailIndex)

    def reactForAnswersMailOptions(self, answer, folder, mailIndex):
        match answer:
            case 0:
                folder.deleteMail(mailIndex)
            case 1:
                whereName = input("where? ")
                self.getFolderOfActive(whereName).append(folder.mails[mailIndex])
                folder.deleteMail(mailIndex)
            case 2:
                content = input("Enter your Answer (Dont hit enter unless your finished. For linebreaks use \\n): ")
                attachmentsPath = input("Enter filepath to your attachement in the attachements folder (PATH or leave blank): ")
                safety = input("Do you want to send the message? (y/n) ")

                if(self.checkSafetyQuestion(safety)):
                    topic = "AW: ", folder.mails[answer].topic
                    content = content + "Original Message: ", folder.mails[answer].content
                    attachmentsPath = folder.mails[answer].attachmentsPath + attachmentsPath
                    self.active.sendMail(topic, folder.mails[answer].sender, self.active.mail, folder.mails[answer].bcc, folder.mails[answer].cc, content, attachmentsPath)
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
    
    def reactForAnswersNoLogin(self, answer):
        match answer:
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

    def askForActionsLogin(self):
        print(self.TEXTdivider)
        print("MENU")
        print(self.TEXTdivider)

        print("What do you want to do?")
        print("0: STOP")
        print("1: Logout")
        print("2: Write an Email")
        print("3: Open Folder")
        out = input("A: ")
        return out
    
    def reactForAnswersLogin(self, answer):
        match answer:
            case "0":
                self.running = False
            case "1":
                self.logout()
            case "2":
                self.writeMail()
            case "3":
                self.selectFolder()
            case _:
                print("LOL")

    #####################Mainloooooooooooooooooooooooooooooooooooooooooooooooooop#################
    def mainloop(self):
        while (self.running):
            print(self.TEXTspacer)
            print(self.TEXTdivider)
            if (not self.active):
                print("**Not logged into an account!**")

                q = self.askForActionsNoLogin()
                self.reactForAnswersNoLogin(q)
                
            else:
                print("********User: ", self.active.userName, "********")

                q = self.askForActionsLogin()
                self.reactForAnswersLogin(q)