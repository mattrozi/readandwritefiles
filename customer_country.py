# python program that reads the file customers.csv and produces a new file containing the customer name and country they are from

import csv


def main():

    infile = open("customers.csv", "r")

    customer = csv.reader(infile, delimiter=",")

    outfile = open("customer_country.csv", "w")
    counter = 0

    for record in customer:
        firstname = record[1]
        lastName = record[2]
        Country = record[4]
        counter += 1
        outfile.write(firstname + "," + lastName + "," + Country + "\n")
    print("The total number of Customers are: " + str(counter - 1))

    outfile.close()
    infile.close()


main()
