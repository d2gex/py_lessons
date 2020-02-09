#  Return soon, Return often
def check_login(username, password, credentials):

    if username == credentials['login'] and password == credentials['password']:
        return 'it is correct'

    if username != credentials['login'] and password == credentials['password']:
        return 'only login ID correct'

    if username == credentials['login'] and password != credentials['password']:
        return 'only password correct'

    return 'none correct'


def get_credentials(filepath):
    with open(filepath, 'r') as fh:
        lines = [line.strip('\n') for line in fh]
    login, login_value = lines[0].split(':')
    password, password_value = lines[-1].split(':')
    return {
        login: login_value,
        password: password_value
    }