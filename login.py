#  Return soon, Return often
def login_2(username, password, credentials):

    if username == credentials['login'] and password == credentials['password']:
        return 'it is correct'

    if username != credentials['login'] and password == credentials['password']:
        return 'only login ID correct'

    if username == credentials['login'] and password != credentials['password']:
        return 'only password correct'

    return 'none correct'
