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
        
def checkForExistingContactUsername(self, userName):
        for i in self.contacts:
            if (i.userName == userName):
                return True
        return False
    
def TEXTnoUserWithUserContactAvailable(self, userName):
        return "No Contact with Username " + userName + " was found!"
    
    
def addNewContactQ(self):
    self.TEXTheading("ADD CONTACT")
    
    userName = input("What is the username of your contact?: ")
    if self.checkForExistingContactUsername(userName):
        print(f"The username {userName} does already exist in your contact list!")
        return
    userName = input("What is the username of your contact?: ")
    firstName = input("What's the firstname of your contact?: ")
    lastName = input("What's the lastname of your contact?: ")
    mail = input("What's the mail of your contact?: ")
    name=("Under which name would you ike to save tis contact?: ")
    self.conatcts.append(Contact(name,userName, firstName, lastName, mail))
    print(f"{userName} was added as {name} to your contacts")
    
def deleteConact(self):
    self.TEXTheading("DELETING CONTACT")
    name =input("What is the name of the Contact you would like to delete?:")
    
    contactRemove = next((contact for contact in self.contacts if contact.name == name), None)
    if contactRemove:
        self.contacts.remove(contactRemove)
        print(f"{name} was removed from your contacts")
        return True
    else:
        print(f"The name: {name} was not found in your contacts.")
        return False
    
def editContact(self):
    
    name = input("What's the name of the contact you want to change?: ")
    for contact in self.contacts:
        if contact.name == name:
            newName = input("How would you like to name this contact?: ")
            contact.name =newName
            print(f"The contac's name has been updated to {name}")
            return
        else:
            print(f"No contact with the name: {name} was found")
        
def specificQuestionnaire(self, answer):
        if (not self.active):
            match answer:
                case 1:
                    self.addNewContactQ()
                case 2:
                    self.deleteConact()
                case 3:
                    self.editContact()
        else:    
            match answer:
                case 1:
                    self.logout()
                case 2:
                    self.writeMail()
                case 3:
                    self.openFolder()

