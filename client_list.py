# This python program that prints out a client list with numbering from the file - clients.txt


def main():
    outfile = open("clients.txt", "r")
    counter = 1

    for client in outfile:
        print(counter, ".", client.rstrip("\n"), sep="")
        counter += 1

    outfile.close()


main()
