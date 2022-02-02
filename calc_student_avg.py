# using the file student_scores.csv
# calculate the average score of each student and save it to a new csv file named student_avg.csv


import csv


def main():
    infile = open("student_scores.csv", "r")

    students = csv.reader(infile, delimiter=",")

    outfile = open("student_avg.csv", "w")
    counter = 0

    for record in students:
        firstname = record[0]
        lastName = record[2]
        Country = record[4]
        counter += 1
        outfile.write(firstname + "," + lastName + "," + Country + "\n")
    print("The total number of Customers are: " + str(counter - 1))

    outfile.close()
    infile.close()
