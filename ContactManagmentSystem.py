from System import System
from Contact import Contact 

class ContactManagementSystem(System):
    def __init__(self):
        super().__init__()
        #These are System specific vars
        self.title = "Contacts"
        self.baseQuestion = '''
What do you want to do?
0: STOP
1: add new Contact
2: delete Conatct 
3: edit Contact
'''
        self.contacts = []
        self.UserManager = False
        
    def checkForExistingContactUsername(self, name):
            for i in self.contacts:
                if (i.name == name):
                    return True
            return False
        
    def TEXTnoUserWithUserContactAvailable(self, userName):
            return "No Contact with Username " + userName + " was found!"
        
        
    def addNewContactQ(self):
        self.TEXTheading("ADD CONTACT")
        
        name = input("Name your Contact: ")
        if self.checkForExistingContactUsername(name):
            print(f"The username {name} does already exist in your contact list!")
            return
        firstName = input("What's the firstname of your contact?: ")
        lastName = input("What's the lastname of your contact?: ")
        mail = input("What's the mail of your contact?: ")
        self.contacts.append(Contact(name, firstName, lastName, mail, self.UserManager.active.userName))
        print(f"{name} was added to your contacts")
        
    def deleteConactQ(self):
        self.TEXTheading("DELETING CONTACT")

        name = input("What is the name of the Contact you would like to delete?: ")

        if self.deleteContact(name):
            print(f"{name} was removed from your contacts")
            return True
        else:
            print(f"The name: {name} was not found in your contacts.")
            return False
        
    def deleteContact(self, name):
        contact = self.getContact(name)
        if contact:
            self.contacts.remove(contact)
            return True
        return False
        
    def getContact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def editContactQ(self):
        name = input("What's the name of the contact you want to change?: ")
        if (self.checkForExistingContactUsername(name)):
            newName = input("How would you like to name this contact?: ")
            newFirstName = input("What's the firstname of your contact?: ")
            newLastName = input("What's the lastname of your contact?: ")

            self.editContact(name, newName, newFirstName, newLastName)
            print(f"{name} was changed to {newName}")
            return True
        print(f"{name} was not found in your contacts")
        return False
    
    def editContact(self, name, newName, newFirstName, newLastName):
        contact = self.getContact(name)
        contact.name = newName
        contact.firstName = newFirstName
        contact.lastName = newLastName
        
            
    def specificQuestionnaire(self, answer):
        if (not self.active):
            match answer:
                case 1:
                    self.addNewContactQ()
                case 2:
                    self.deleteConactQ()
                case 3:
                    self.editContactQ()
        else:    
            match answer:
                case 1:
                    self.logout()
                case 2:
                    self.writeMail()
                case 3:
                    self.openFolder()

