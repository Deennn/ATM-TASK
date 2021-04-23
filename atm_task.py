import random
from datetime import datetime

# Register
# -Username,password, Email
# - Generate user account


# Login
# -(Username or email) and password


# Initializing the system
Database = {
    3368834322: ['joe@gmail.com', "adebowale", "joe", "joe10", 0],
    1962942985: ["dele@yahoo.com", "delebo", "lucas", "del12", 0],
    4857136410: ["bola@fmail.com", "bolade", "kike", "kide", 0],
}


def init():
    """
    A initializing function that initialize the whole program.
    :return:Get the program started.
    """

    print("Welcome to Zuri_Bank")
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(current_time)

    have_account = int(input("Do you have an account with us:\n1 (yes) 2 (no)\n"))
    if have_account == 1:
        login()
    elif have_account == 2:

        register()
    else:
        print("You have selected an invalid option")
        init()


def login():
    """
    A login function that asks for the user account number and password and check the database to see if it exist or is
    correct.
    :return:Logged the user if put a valid account number and password
    """
    print("******** Login ********")
    user_account_number = (input("Enter your account number:\n"))
    is_valid_account_number = account_number_validation(user_account_number)
    if is_valid_account_number:

        Password = input("Enter your password:\n")

        for account_number, user_details in Database.items():
            if account_number == int(user_account_number):
                if user_details[3] == Password:
                    bank_operation(user_details)

        print("Invalid account or password")
        login()
    else:
        init()


def account_number_validation(account_number):
    """

    :param account_number: Take account number as a parameter to check if it's valid.
    :return: Get through if the account number is valid i.e True otherwise False
    """
    if account_number:

        if len(str(account_number)) == 10:

            try:
                int(account_number)
                return True
            except ValueError:
                print("Invalid account number, account number can only be integer")
        else:
            print("Account number cannot be more than or less than 10 digits")
            return False

    else:
        print("Account number is a required field")
        return False


def register():
    """
    A function that take in some user details
    :return: return a well formatted statement of the account created with account number.
    """
    print("****** Register *******")
    email = input("Enter your email address:\n ")
    first_name = input("Enter your first name:\n ")
    last_name = input("Enter your last name:\n ")
    password = input("Create password:\n")

    try:
        account_number = generate_account_number()
    except ValueError:

        print("account generation failed.")
        init()

    Database[account_number] = [first_name, last_name, email, password, 0]

    print("Your account have been successfully created")
    print("your account number is {}".format(account_number), "Keep it safe")
    login()


def bank_operation(user_details):
    """
    A function about the available banking option available for the user
    :param user_details: user_details
    :return: A well formatted string welcoming the user and asking what he wnt to do.
    """
    print("Welcome {} {}".format(user_details[1].title(), user_details[2].title()))

    selected_option = int(input("What would you like to do?\n(1) deposit\n(2) withdrawal\n(3) transfer\n(4) balance\n"
                                "(5) login\n(6) exit\n"))

    if selected_option == 1:
        deposit()
    elif selected_option == 2:
        withdrawal()
    elif selected_option == 3:
        transfer()
    elif selected_option == 4:
        balance_check()
    elif selected_option == 5:
        login()
    elif selected_option == 6:
        exit()
    else:
        print("Invalid option selected")
        bank_operation(user_details)


def balance_check():
    """
    A function that check user balance
    :return: Return a well formatted string of the user balance
    """
    for account_number, user_details in Database.items():
        balance = user_details[4]
        print("Your account balance is {}".format(balance))
        other_transaction()


def deposit():
    """
    A deposit function that asks the user how much they would like to deposit
    :return: Return a well formatted string of how the user deposit and how much their balance is.
    """
    for account_number, user_details in Database.items():
        balance = user_details[4]
        deposit_amount = int(input("How much would like to deposit?\n"))
        balance += deposit_amount
        user_details[4] = balance
        print("you've deposited {} to your account".format(deposit_amount))
        print("Your account balance is now {}".format(balance))
        other_transaction()


def withdrawal():
    """
    A withdrawal function that the user how much they would like to withdrawal
    :return: Return a well formatted string of how much they withdraw # you can't withdraw what you don't have.

    """
    for account_number, user_details in Database.items():
        balance = user_details[4]
        withdrawal_amount = int(input("How much would you like to withdraw?\n"))
        if withdrawal_amount > balance:
            print("Insufficient fund, you account balance is {}".format(balance))
            other_transaction()
        else:
            balance -= withdrawal_amount
            print("You've successfully withdraw {} and your current account balance is {}".format(withdrawal_amount,
                                                                                                  balance))
            user_details[4] = balance
            other_transaction()


def transfer():
    """
    A transfer function that ask the user their transfer destination and how they would like to transfer.
    :return: Return a well formatted string of how they transfer and where to.
    """
    for account_number, user_details in Database.items():
        balance = user_details[4]
        transfer_destination = int(input("Enter destination account number:\n"))
        for t_account_number, t_user_details in Database.items():
            transfer_balance = t_user_details[4]
            if transfer_destination in Database:
                transfer_amount = int(input("Enter transfer amount:\n"))
                if transfer_amount > balance:
                    print("Insufficient fund, try again")
                    other_transaction()

                else:
                    balance -= transfer_amount
                    transfer_balance += transfer_amount
                    print("you've successfully transfer {} to {} {}".format(transfer_amount, t_user_details[1].title(),
                                                                            t_user_details[2].title()))
                    t_user_details[4] = transfer_balance
                    user_details[4] = balance
                    other_transaction()

            else:
                print("Invalid account number")
                other_transaction()


def generate_account_number():
    """
    A function that generate account number for registered user
    :return: Return the generated account number
    """
    return random.randrange(1111111111, 9999999999)


def other_transaction():
    """
    A function that help to perform another transaction.
    :return:
    """
    for account_number, user_details in Database.items():
        another_transaction = int(input("Would you like to perform another transaction?\n(1) yes (2) no\n"))
        if another_transaction == 1:
            bank_operation(user_details)
        else:
            exit()


init()

# ACTUAL BANKING SYSTEM #
