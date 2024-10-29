import csv
from tabulate import tabulate


# TO ADD BOOKS TO RECORD
def add_book():
    name = input("Enter Name of the book: ")
    author = input("Enter Name of the author")
    dl = int(input("Enter published date(in ddmmyy format, example - 030708): "))
    review = int(input("Enter the review on goodreads: "))
    with open('data.csv', 'a') as file1:
        writer = csv.writer(file1)
        writer.writerow([name, author, dl, review])
        print("Book is added!!")
    file1.close()
fff



# TO DELETE RECORDS
def del_book():
    delname = input("Enter the name of the book to be deleted(no spaces): ")
    with open('data.csv', 'r') as file2, open('data.csv', 'w') as file4:
        reader = csv.reader(file2)
        writer = csv.writer(file4)
        for q in reader:
            if q[0] == delname:
                writer.writerow(q)
            else:
                pass
    file4.close()
    file2.close()





# TO SHOW ALL THE BOOKS

def show_book():
    with open('data.csv', 'r') as file3:
        readfile = csv.reader(file3)
        print(tabulate(readfile, headers = ['NAME', 'AUTHOR', 'DATE OF PUBLISH', 'RATING']))
    file3.close()


# MAIN
t = True

print("\nWELCOME TO THE LIBRARY RECORDS\n")
while t:
    print("-------------------------------\n")
    print("Select any one of the following options")
    print("1: Show Records of all the books that are in our Library")
    print("2. Add record for a new book")
    print("3. Delete record of book by name")
    print("4: Exit program")
    print("\n----------------------------------")

    choice = int(input("Enter Choice: "))
    if choice == 1:
        show_book()
    elif choice == 2:
        add_book()
    elif choice == 3:
        del_book()
    elif choice == 4:
        print("Thankyouuu")
        t = False
    else:
        print('Entered choice is invalid')


