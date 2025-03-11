class HoursAndSales:
    def __init__(self, id, employeeId, date, sales, hoursWorked):
        self.id = id
        self.employeeId = employeeId
        self.date = date
        self.sales = sales
        self.hoursWorked = hoursWorked

    def __str__(self):
        return f'{self.id}: employee: {self.employeeId}, {self.date}, sales: {self.sales}, hours: {self.hoursWorked}'