import login


if __name__ == '__main__':
    login_entered = input('enter the login ID ')
    password_entered = input('enter the password ')
    result = login.login_2(login_entered, password_entered)
    print(result)

