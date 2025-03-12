import csv
import os

def createPayslip(data, employee):
    daily_data = []
    # Calculate daily and total earnings
    for day_data in data:
        commission = (day_data.sales or 0) * employee.comissionRate
        total_daily_earnings = (day_data.hoursWorked or 0) * employee.baseSalary + commission
        daily_data.append({"date": day_data.date, "hours worked": (day_data.hoursWorked or 0), "sales": (day_data.sales or 0), "base salary": employee.baseSalary, "commission rate": employee.comissionRate, "daily earning": total_daily_earnings})

    total_overall_earnings = sum(day["daily earning"] for day in daily_data)

    print(daily_data)

    # Write data to CSV
    fileName = "Payslip-" + data[0].date + "-" + employee.name + ".csv"
    filePath = os.path.join("db", "payslips", fileName)
    with open(filePath, mode="w", newline="") as csvfile:
        fieldnames = ["date", "hours worked", "sales", "base salary", "commission rate", "daily earning"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for day_data in daily_data:
            writer.writerow(day_data)

    # Append total overall earnings
    with open(filePath, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([])  # Empty row for separation
        writer.writerow(["Total Overall Earnings", total_overall_earnings])

    return filePath