
LOGIN = 'abc'
PASSWORD = '123'


#  Return soon, Return often
def login_2(username, password):

    if username == LOGIN and password == PASSWORD:
        return 'it is correct'

    if username != LOGIN and password == PASSWORD:
        return 'only login ID correct'

    if username == LOGIN and password != PASSWORD:
        return 'only password correct'

    return 'none correct'
