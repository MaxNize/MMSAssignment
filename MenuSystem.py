from System import System


class MenuSystem(System):
    def __init__(self, accountingManager, mailManager, employeeManager):
        super().__init__()
        self.title = "SYSTEM MENU"
        self.baseQuestion = '''
What do you want to do?
0: STOP
1: enter Employee System
2: enter Accounting System
3: enter Mail System
'''
        self.accountingManager = accountingManager
        self.mailManager = mailManager
        self.employeeManager = employeeManager

    def specificQuestionnaire(self, answer):
        match answer:
            case 1:
                self.employeeManager.mainloop()
            case 2:
                self.accountingManager.mainloop()
            case 3:
                self.mailManager.mainloop()