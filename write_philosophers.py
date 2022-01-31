# This Program writes three lines of data to a file


def main():
    outfile = open("philosophers.txt", "w")
    outfile.write("John Locke" + "\n")
    outfile.write("David Hume" + "\n")
    outfile.write("Edmund Burke" + "\n")

    outfile.close()


def add_my_name():
    outfile = open("philosophers.txt", "a")
    outfile.write("Matt Rozinskas\n")
    outfile.close()


main()
add_my_name()
