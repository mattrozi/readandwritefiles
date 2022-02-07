# using the file student_scores.csv
# calculate the average score of each student and save it to a new csv file named student_avg.csv


import csv


def main():
    infile = open("student_scores.csv", "r")

    students = csv.reader(infile, delimiter=",")

    outfile = open("student_avg.csv", "w")
    counter = 0
    outfile.write("Name,Average Score \n")

    for record in students:
        Name = record[0]
        Score1 = int(record[1])
        Score2 = int(record[2])
        Score3 = int(record[3])
        averageScore = round((Score1 + Score2 + Score3) / 3, 2)
        outfile.write(Name + "," + str(averageScore) + "\n")

    outfile.close()


main()
