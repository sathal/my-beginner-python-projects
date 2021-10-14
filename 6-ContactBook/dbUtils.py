import apsw

database = "contactBook"

greeeting = """
Greetings. This program is a simple demo of a basic contact book implementation using SQLite and Python
"""

options = """
Please enter one of the following:
    'l' - list all contacts in the database
    'a' - add a new contact to the database
    'e' - edit an existing contact in the database
    'd' - delete an existing contact from the database
Your response: """


def initializeDatabase():
    global database

    createTable = """
        CREATE TABLE IF NOT EXISTS contacts (
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            UNIQUE(phone_number)
            );
    """

    try:
        connection=apsw.Connection(database)
        cursor=connection.cursor()
        cursor.execute(createTable)
    except:
        print("ERROR: Encountered issue on upon setup. Exiting...")


def deleteContact():
    global database
    print("Indicate a single entry you would like to REMOVE by entering the corresponding ID:")

    getAllContactRecords = "select rowid,first_name,last_name,phone_number from contacts"

    try:
        connection=apsw.Connection(database)
        cursor=connection.cursor()

        # This is the preferred way for obtaining all of the results from a query
        rows = list( cursor.execute(getAllContactRecords) )

        for resultIndex, row in enumerate(rows):
            print("\t" + str(row))

    except:
        print("ERROR: Encountered issue when attempting list out entries...")

    try:
        id = input("ID of entry you wish to delete: ")

        idFound = False
        nameDeleted = ""

        for row in rows:
            if str(row[0]) == id:
                idFound = True
                nameDeleted = row[1] + " " + row[2]
                break

        if idFound == False:
            print("ERROR: " + id + " is not a valid option...")
            return

        deleteRecord = "delete from contacts where rowid = ?"
        connection=apsw.Connection(database)
        cursor=connection.cursor()
        cursor.execute(deleteRecord,(id))
        print(nameDeleted + " has been removed from the contact book...")
    except:
        print("ERROR: Encountered issue when attempting delete id " + id + "...")


def editContact():
    global database
    editPromptText = """
    Enter the number for the corresponding field you wish to edit:
        1 - First Name
        2 - Last Name
        3 - Phone Number

    Your Selection: """

    print("Indicate a single entry you would like to EDIT by entering the corresponding ID:")

    getAllContactRecords = "select rowid,first_name,last_name,phone_number from contacts"

    try:
        connection=apsw.Connection(database)
        cursor=connection.cursor()

        # This is the preferred way for obtaining all of the results from a query
        rows = list( cursor.execute(getAllContactRecords) )

        for resultIndex, row in enumerate(rows):
            print("\t" + str(row))

    except:
        print("ERROR: Encountered issue when attempting list out entries...")

    try:
        id = input("ID of entry you wish to edit: ")

        idFound = False
        firstNameToEdit = ""
        lastNameToEdit = ""
        phoneNumberToEdit = ""

        for row in rows:
            if str(row[0]) == id:
                idFound = True
                firstNameToEdit = row[1]
                lastNameToEdit = row[2]
                phoneNumberToEdit = row[3]
                break

        if idFound == False:
            print("ERROR: " + id + " is not a valid option...")
            return

        editOption = input(editPromptText)

        if editOption == "1":
            newValue = input("Enter a new first name: ")
            if validateName(newValue) == False:
                print("ERROR: " + newValue + " is not a valid first name...")
                return
            updateQuery = "update contacts set first_name = ? where rowid = ?"
        elif editOption == "2":
            newValue = input("Enter a new last name: ")
            if validateName(newValue) == False:
                print("ERROR: " + newValue + " is not a valid last name...")
                return
            updateQuery = "update contacts set last_name = ? where rowid = ?"
        elif editOption == "3":
            newValue = input("Enter a new phone number: ")
            if validatePhoneNumber(newValue) == False:
                print("ERROR: " + newValue + " is not a valid phone number...")
                return
            updateQuery = "update contacts set phone_number = ? where rowid = ?"
        else:
            print("ERROR: " + editOption + " is not a valid option...")
            return

        connection=apsw.Connection(database)
        cursor=connection.cursor()
        cursor.execute(updateQuery,(newValue,id))
        print("Update successful...")
    except:
        print("ERROR: Encountered issue when attempting edit id " + id + "...")




def validateName(firstOrLastName):
    return firstOrLastName.isalpha()

def validatePhoneNumber(phoneNumber):
    return (phoneNumber.isdigit() and len(phoneNumber) == 10)

def validateNewContactInformation(firstName,lastName,phoneNumber):
    return validateName(firstName) and validateName(lastName) and validatePhoneNumber(phoneNumber)

def addContact():
    global database
    print("Add contact")
    firstName = input("First Name: ")
    if validateName(firstName) == False:
        print("'" + firstName + "' is not a valid first name...")
        return
    lastName = input("Last Name: ")
    if validateName(lastName) == False:
        print("'" + lastName + "' is not a valid last name...")
        return
    phoneNumber = input("Phone Number: ")
    if validatePhoneNumber(phoneNumber) == False:
        print("'" + phoneNumber + "' is not a valid phone number. Must used following format: 9999999999")
        return

    # If we get to this point then the data can be considered valid

    insertQuery = "insert into contacts values(?,?,?)"
    connection=apsw.Connection(database)
    cursor=connection.cursor()
    try:
        cursor.execute(insertQuery,(firstName,lastName,phoneNumber))
        print("Successfully added " + firstName + " " + lastName + ' ' + "to the contact book...")
    except:
        print("ERROR: Encountered issue when trying to add " + firstName + " " + lastName + ' ' + "to the contact book...")


def listAllContacts():
    global database
    print("These are your contacts:")

    getAllContactRecords = "select * from contacts"

    try:
        connection=apsw.Connection(database)
        cursor=connection.cursor()

        # This is the preferred way for obtaining all of the results from a query
        rows = list( cursor.execute(getAllContactRecords) )

        for row in rows:
            print("\t" + str(row))
    except:
        print("ERROR: Encountered issue when attempting to list all contacts in the contact book...")
