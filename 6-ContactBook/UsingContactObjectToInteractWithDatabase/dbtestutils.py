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


class Contact:
    def __init__(self,rowid,first_name,last_name,phone_number):
        self.rowid = rowid
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

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
            firstNameToEdit = input("Enter a new first name: ")
            if validateName(firstNameToEdit) == False:
                print("ERROR: " + firstNameToEdit + " is not a valid first name...")
                return
        elif editOption == "2":
            lastNameToEdit = input("Enter a new last name: ")
            if validateName(lastNameToEdit) == False:
                print("ERROR: " + lastNameToEdit + " is not a valid last name...")
                return
        elif editOption == "3":
            phoneNumberToEdit = input("Enter a new phone number: ")
            if validatePhoneNumber(phoneNumberToEdit) == False:
                print("ERROR: " + phoneNumberToEdit + " is not a valid phone number...")
                return
        else:
            print("ERROR: " + editOption + " is not a valid option...")
            return

        editedContact = Contact(id,firstNameToEdit,lastNameToEdit,phoneNumberToEdit)

        connection=apsw.Connection(database)
        cursor=connection.cursor()
        cursor.execute("update contacts set first_name = ?, last_name = ?, phone_number = ? where rowid = ?",(editedContact.first_name,editedContact.last_name,editedContact.phone_number,editedContact.rowid))
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

    newContact = Contact(0, firstName, lastName, phoneNumber)

    connection=apsw.Connection(database)
    cursor=connection.cursor()
    try:
        cursor.execute("insert into contacts values(?,?,?)",(newContact.first_name, newContact.last_name, newContact.phone_number))
        print("Successfully added " + newContact.first_name + " " + newContact.last_name + ' ' + "to the contact book...")
    except Exception as ex:
        print("ERROR: Encountered issue when trying to add " + newContact.first_name + " " + newContact.last_name + ' ' + "to the contact book...")
        print(ex)

def listAllContacts():
    global database
    print("These are your contacts:")

    contactObjectList = list()

    getAllContactRecords = "select rowid,first_name,last_name,phone_number from contacts"

    try:
        connection=apsw.Connection(database)
        cursor=connection.cursor()

        # This is the preferred way for obtaining all of the results from a query
        rows = list( cursor.execute(getAllContactRecords) )

        for row in rows:
            #print("Attempting to create Contact object with the following: ")
            #print(*row)
            contactObjectList.append(Contact(*row))

        for obj in contactObjectList:
            print(str(obj.rowid) + " " + obj.first_name + " " + obj.last_name + " " + obj.phone_number)

    except Exception as ex:
        print("ERROR: Encountered issue when attempting to list all contacts in the contact book...")
        print(ex)
