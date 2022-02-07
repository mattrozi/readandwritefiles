# python program that reads the employeepay.csv file and prints out details of each employee

import csv


def main():

    employee = open("EmployeePay.csv", "r")

    Employee_file = csv.reader(employee, delimiter=",")

    # To skip a line if the file contains a header record
    next(Employee_file)

    for record in Employee_file:
        Id = record[0]
        FirstName = record[1]
        lastName = record[2]
        Salary = record[3]
        Bonus =round(int(record[3])*float(record[4]),2)
        totalPay=format(int(Salary)+round(Bonus,2),',.2f')

        print(
            "First Name: "
            + FirstName
            + "\n"
            + "Last Name: "
            + lastName
            + "\n"
            + "Salary: $"
            + Salary
            + "\n"
            + "Bonus: "
            + str(Bonus)
            + "\n"
            +"Total Pay: $"+
            str(totalPay)+'\n'


    
            
        )


main()
