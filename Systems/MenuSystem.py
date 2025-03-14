from Abstracts.System import System


class MenuSystem(System):
    def __init__(self, mailManager, employeeManager):
        super().__init__()
        self.title = "SYSTEM MENU"
        self.baseQuestion = '''
What do you want to do?
0: STOP
1: enter Employee System
2: enter Mail System
'''
        self.mailManager = mailManager
        self.employeeManager = employeeManager

    def specificQuestionnaire(self, answer):
        match answer:
            case 1:
                self.employeeManager.mainloop()
            case 2:
                self.mailManager.mainloop()