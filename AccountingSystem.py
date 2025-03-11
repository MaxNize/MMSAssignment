from System import System


class AccountingSystem(System):
    def __init__(self):
        super().__init__()
        self.title = "ACCOUNTING"
        self.baseQuestion = '''
What do you want to do?
0: return to menu
'''