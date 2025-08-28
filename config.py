import configparser

config = configparser.ConfigParser()

config.read('config.ini')

def get_login_data() -> tuple[str, str]:
    login = config['LOGIN_DATA']['login']
    password = config['LOGIN_DATA']['password']
    return (login, password)
