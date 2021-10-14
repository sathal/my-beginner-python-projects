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
        CREATE TABLE IF NOT EXISTS CONTACTS (
            ID INTEGER PRIMARY KEY,
            FIRST_NAME TEXT NOT NULL,
            LAST_NAME TEXT NOT NULL,
            PHONE_NUMBER TEXT NOT NULL
            );
    """

    connection=apsw.Connection(database)
    cursor=connection.cursor()
    cursor.execute(createTable)

def deleteContact():
    print("Delete contact")

def editContact():
    print("Edit contact")

def validateName(firstOrLastName):
    return firstOrLastName.isalpha()

def validatePhoneNumber(phoneNumber):
    return (phoneNumber.isdigit() and len(phoneNumber) == 10)

def validateNewContactInformation(firstName,lastName,phoneNumber):
    return validateName(firstName) and validateName(lastName) and validatePhoneNumber(phoneNumber)

def addContact():
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

    if validateNewContactInformation(firstName,lastName,phoneNumber):
        # Insert new contact into the initializeDatabase
        print("Saving to database... (jk)")
    else:
        print("One or more of the specified fields included invalid contact information...")



def listAllContacts():
    print("List all contacts")

    getAllContactRecords = "select * from CONTACTS"

    connection=apsw.Connection(database)
    cursor=connection.cursor()

    # This is the preferred way for obtaining all of the results from a query
    rows = list( cursor.execute(getAllContactRecords) )

    for row in rows:
        print(row)
