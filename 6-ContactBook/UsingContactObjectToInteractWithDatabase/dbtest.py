import dbtestutils


def main():

    ### Greeting message
    print(dbtestutils.greeeting)

    ### Ensure we've got a database to work with
    dbtestutils.initializeDatabase()

    ### Present to the user the valid list of options
    userResponse = input(dbtestutils.options)

    ### Continue to accept user input until user decides to quit by entering 'q'
    while userResponse != 'q':
        if userResponse == 'l':
            dbtestutils.listAllContacts()
        elif userResponse == 'a':
            dbtestutils.addContact()
        elif userResponse == 'e':
            dbtestutils.editContact()
        elif userResponse == 'd':
            dbtestutils.deleteContact()
        else:
            print('...INVALID Input')

        userResponse = input(dbtestutils.options)

    print('Exiting...')


main()
