#in this file everything concering contacts is handeled
from datetime import datetime
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
'''     
# Variables and functions used for cheking 
        self.UserManager = False
        self.active = False
        
    def checkForExistingContactUsername(self, name):
            for i in self.active.contacts:
                if (i.name == name):
                    return True
            return False
        
    def TEXTnoUserWithUserContactAvailable(self, userName):
            return "No Contact with Username " + userName + " was found!"
        
#mainfunction 1 adds a contact to to the contact table
    def addNewContactQ(self):
        self.TEXTheading("ADD CONTACT")
        
        while True:
            name = input("Name your Contact: ")
            if self.checkForExistingContactUsername(name):
                print(f"The username {name} does already exist in your contact list!")
                continue
            firstName = input("What's the firstname of your contact?: ")
            lastName = input("What's the lastname of your contact?: ")
            phone =input("Please enter their phonenumber: ")
            mail = input("What's the mail of your contact?: ")
            if not self.checkForMailpattern(mail):
                 print("Invalid mail entered! Please try again.")
                 continue
            self.active.contacts.append(Contact(name, firstName, lastName, mail, self.UserManager.active.userName, phone))
            print(f"{name} was added to your contacts")
            break
        
    def deleteContactQ(self, name):
        self.TEXTheading("DELETING CONTACT")

        if (self.checkSafetyQuestion(input("Are you sure you want to delete that contact? (y/n) "))):
            if self.deleteContact(name):
                print(f"{name} was removed from your contacts")
                return True
            else:
                print(f"Error")
                return False
        
    def deleteContact(self, name):
        contact = self.getContact(name)
        if contact:
            self.active.contacts.remove(contact)
            return True
        return False
        
    def getContact(self, name):
        for contact in self.active.contacts:
            if contact.name == name:
                return contact
        return None

    def editContactQ(self, name):
        while True:
            newName = input("How would you like to name this contact?: ")
            if (self.checkForExistingContactUsername(newName)):
                print(f"The username {newName} does already exist in your contact list!")
                continue
            newFirstName = input("What's the firstname of your contact?: ")
            newLastName = input("What's the lastname of your contact?: ")
            newPhoneNumber = input("What's the phonenumebr of your contact?: ")
            newMail = input("What's the mail of your contact?: ")
            if (not self.checkForMailpattern(newMail)):
                print("Invalid mail entered! Please try again.")
                continue
            if (not self.checkSafetyQuestion(input("Are you sure you want to change this contact? (y/n) "))):
                return False
            self.editContact(name, newName, newFirstName, newLastName, newPhoneNumber, newMail)
            print(f"{name} was changed to {newName}")
            return True
        
    def sendMailToContact(self, mail):
        self.TEXTheading("WRITE MAIL")

        subject = input("Enter subject: ")
        to = mail
        if (self.checkForMailpattern(to)):
            bcc = input("Enter Bcc (or leave blank): ")
            cc = input("Enter Cc (or leave blank): ")
            content = input("Enter your mail (Dont hit enter unless your finished. For linebreaks use \\n): ")
            attachmentsPath = input("Enter filepath to your attachement in the attachements folder (PATH or leave blank): ")
            time = datetime.now()
            time = time.strftime("%Y-%m-%d %H:%M:%S")
            safety = input("Do you want to send the message? (y/n) ")
            if(self.checkSafetyQuestion(safety)):
                self.active.sendMail(subject, to, self.active.mail, bcc, cc, content, attachmentsPath, time)
                print("The Mail has been added to your Outbox!")
        else:
            print("That's not an email!")
            self.writeMail()
    
    def editContact(self, name, newName, newFirstName, newLastName, newPhoneNumber, newMail):
        contact = self.getContact(name)
        contact.name = newName
        contact.firstName = newFirstName
        contact.lastName = newLastName
        contact.phoneNumber = newPhoneNumber
        contact.mail = newMail
  
#mainfunction 4 outputs a list with all the names of the useres contacts 
    def updateBaseQuestion(self):
        if (not self.active or len(self.active.contacts) == 0 ):
            self.baseQuestion = '''
What do you want to do?
0: Close contacts
1: add new Contact
You currently have no Contacts 
'''
            return
        self.baseQuestion = '''
What do you want to do?
0: Close contacts
1: add new Contact
'''
        j = 2
        for i in self.active.contacts:
            self.baseQuestion = self.baseQuestion+ str(j) + ": " +"name: "+i.name + "\n"
            j += 1    

    def openContact(self, contactIndex):
        self.TEXTheading(self.active.contacts[contactIndex].name)
        question = ''''''
        question += f"Firstname: {self.active.contacts[contactIndex].firstName}\n"
        question += f"Lastname: {self.active.contacts[contactIndex].lastName}\n"
        question += f"Mail: {self.active.contacts[contactIndex].mail}\n"
        question += f"phone: {self.active.contacts[contactIndex].phone}\n"
        question += '''
What do you want to do?
0: Close contact
1: Delete contact
2: Edit contact
3: Send mail to contact
'''

        while True:
            answer = self.safeQuestion(question, "int")
            if (answer == 0):
                return
            if (answer == 1):
                self.deleteContactQ(self.active.contacts[contactIndex].name)
                return
            if (answer == 2):
                self.editContactQ(self.active.contacts[contactIndex].name)
                return
            if (answer == 3):
                self.sendMailToContact(self.active.contacts[contactIndex].mail)
                return
            print("No such option")
            
    def updateBasedOnActivity(self):
        self.updateBaseQuestion()
    
    def initing(self):
        self.updateBasedOnActivity()
    
    #here are the switch case statments to execute the mainfunctions of this file
    def specificQuestionnaire(self, answer):
        if (not self.active):
            pass  
        else:    
            match answer:
                case 1:
                    self.addNewContactQ()
                case _:
                    self.openContact(answer-2)

