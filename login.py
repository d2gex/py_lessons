
LOGIN = 'abc'
PASSWORD = '123'
#
#
# login_entered = input('enter the login ID ')
# password_entered = input('enter the password ')
#


def login(username, password):
    if username == LOGIN and password == PASSWORD:
        verdict = 'it is correct'
    elif username != LOGIN and password == PASSWORD:
        verdict = 'only login ID correct'
    elif username == LOGIN and password != PASSWORD:
        verdict = 'only password correct'
    else:
        verdict = 'none correct'
    return verdict


#  Return soon, Return often
def login_2(username, password):

    if username == LOGIN and password == PASSWORD:
        return 'it is correct'

    if username != LOGIN and password == PASSWORD:
        return 'only login ID correct'

    if username == LOGIN and password != PASSWORD:
        return 'only password correct'

    return 'none correct'


if __name__ == '__main__':
    login_entered = input('enter the login ID ')
    password_entered = input('enter the password ')
    result = login_2(login_entered, password_entered)
    print(result)
