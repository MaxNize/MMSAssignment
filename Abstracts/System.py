import re #allows the usage of RegEX 
from abc import ABC, abstractmethod

class System:
    def __init__(self):
        #These are for same texts everywhere
        self.TEXTdivider = "********************************"
        self.TEXTspacer = "\n\n\n\n\n\n\n\n\n\n"
        self.emailPattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        self.datePattern = r"(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0,1,2])\.(19|20)\d{2}"
        self.TEXTenterUserName = "Please enter a Username: "
        self.TEXTenterYourPw = "Please enter your Password: "
        #These are the vars every System needs
        self.running = True
        #These are System specific vars
        self.baseQuestion = "Do you want to do something? "
        self.title = "SYSTEM"
        self.active = False

    #System wide used functions
    #we like safe questioning. it makes your program less crashy
    def safeQuestion(self, text, expectedValueType):
        match expectedValueType:
            case "int":
                while (True):
                    try:
                        out = int(input(text))
                        return out
                    except ValueError:
                        print("Input must be an Integer")
            case "date":
                while (True):
                    out = input(text)
                    if re.match(self.datePattern, out):
                        return out
                    else:
                        print("Invalid date format! Please try again. (DD.MM.YYYY)")
            case "mail":
                while (True):
                    out = input(text)
                    if self.checkForMailpattern(out):
                        return out
                    else:
                        print("Invalid mail format! Please try again.")
            case "hourType":
                while (True):
                    out = input(text)
                    if (out == "fulltime" or out == "parttime"):
                        return out
                    else:
                        print("Invalid hourType! Please try again. (must be fulltime or parttime)")
            case "float":
                while (True):
                    try:
                        out = float(input(text))
                        return out
                    except ValueError:
                        print("Input must be a float")

            case "decimalPercentage":
                while (True):
                    try:
                        out = float(input(text))
                        if (out >= 0 and out <= 1):
                            return out
                        else:
                            print("Input must be a decimal between 0 and 1")
                    except ValueError:
                        print("Input must be a decimal")
            case "safety":
                out = input(text)
                if (out == "y" or out == "Y" or out == "yes" or out == "Yes"):
                    return True
                return False
            
    def TEXTheading(self, text):
        print(self.TEXTdivider)
        print(text)
        print(self.TEXTdivider)

    def checkSafetyQuestion(self, input):
        if (input == "y" or input == "Y" or input == "yes" or input == "Yes"):
            return True
        return False

    
    def initing(self):
        pass
    
    def checkForMailpattern(self, string):
        if re.match(self.emailPattern, string):
            return True
        return False
    #alsways ask something
    def baseQuestionnaire(self):
        self.initing()
        print(self.TEXTspacer)
        self.TEXTheading(self.title)
        answer = self.safeQuestion(self.baseQuestion, "int")
        if (answer == 0):
            self.running = False
            return
        self.specificQuestionnaire(answer)

    def specificQuestionnaire(self, answer):
        match answer:
            case 1:
                print("your thing")

    def mainloop(self):
        self.running = True
        while(self.running):
            self.baseQuestionnaire()
        
        self.active = False