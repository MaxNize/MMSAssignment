from System import System
import Contact

class ContactManagementSystem(System):
    def __init__(self):
        super().__init__()
        
        self.contacts = []
        #These are System specific vars
        self.title = "MENU : No User logged in"
        self.baseQuestion = '''
What do you want to do?
0: STOP
1: add new Contact
2: delete Conatct 
3: edit Contact
'''
def addNewContactQ(self,name,userName, firstName, lastName, mail):
    self.conatcts.append(Contact(name,userName, firstName, lastName, mail))
    
def deleteConact(self, name):
        try:
            self.contacts.remove(self.getContacts(name))
            return True
        except:
            return False
        
def changeName(self, name):
        newName = input("What's the contact's new name?")
        self.name = newName
        
def changeMail(self, mail):
        newMail = input("What's the contact's new mail")
        self.mail = newMail
        
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

