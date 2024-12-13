import User

class MailManagementSystem:
    def __init__(self):
        self.users = []
        self.running = True
        self.active = False

    def createUser(self):
        print("********************************")
        userName = input("Please enter a Username: ")
        firstName = input("Please enter a Firstname: ")
        lastName = input("Please enter a Lastname: ")
        mail = input("Please enter a Mail: ")
        pw = input("Please enter a Password: ")
        self.users.append(User.User(userName, firstName, lastName, mail, pw))

    def deleteUser(self, userName):
        for i in self.users:
            if (i.userName == userName):
                self.users.remove(i)

    def logIntoUser(self, userName, pw):
        for i in self.users:
            if (i.userName == userName):
                if(i.login(userName, pw)):
                    self.active = i
                    print("your now Logged in, ", userName,"!")
                    break

        print("No User available")

    def printAvailableUsers(self):
        for i in self.users:
            print(i.userName)

    def askForActions(self):
        print("********************************")
        print("What do you want to do?")
        print("0: STOP")
        print("1: create a new User")
        print("2: log into a User")
        print("3: delete a User")
        out = input("A: ")
        return out

    def mainloop(self):
        while (self.running):
            print("User: ", self.active)

            q = self.askForActions()

            match q:
                case "0":
                    self.running = False
                    print(self.running)
                case "1":
                    self.createUser()
                case _:
                    print("LOL")
