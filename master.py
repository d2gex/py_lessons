import login

if __name__ == '__main__':
    #  we read the credentials from text file
    credentials = login.get_credentials('.credentials')

    #  we get the user's login and password from the keyboard
    login_entered = input('enter the login ID ')
    password_entered = input('enter the password ')

    #  we run our business logic to ensure the credentials are the correct one
    result = login.check_login(login_entered, password_entered, credentials)
    # print(credentials)
    print(result)

