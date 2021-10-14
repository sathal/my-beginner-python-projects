import dbUtils


def main():

    ### Greeting message
    print(dbUtils.greeeting)

    ### Ensure we've got a database to work with
    dbUtils.initializeDatabase()

    ### Present to the user the valid list of options
    userResponse = input(dbUtils.options)

    ### Continue to accept user input until user decides to quit by entering 'q'
    while userResponse != 'q':
        if userResponse == 'l':
            dbUtils.listAllContacts()
        elif userResponse == 'a':
            dbUtils.addContact()
        elif userResponse == 'e':
            dbUtils.editContact()
        elif userResponse == 'd':
            dbUtils.deleteContact()
        else:
            print('...INVALID Input')

        userResponse = input(dbUtils.options)

    print('Exiting...')


main()
