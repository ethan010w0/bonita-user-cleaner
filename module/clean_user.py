import requests

BONTIA_CONFIG = 'Bonita'
BONITA_URL = 'URL'
BONITA_USERNAME = 'Username'
BONITA_PASSWORD = 'Password'

LOGIN_URL = '/loginservice'
LOGOUT_URL = '/logoutservice'
USER_URL = '/API/identity/user'


# Clean User.
def clean_user(config, all):
    # Get config.
    bonita_url = config[BONTIA_CONFIG][BONITA_URL]
    bonita_username = config[BONTIA_CONFIG][BONITA_USERNAME]
    boita_password = config[BONTIA_CONFIG][BONITA_PASSWORD]

    session = requests.Session()

    # Login.
    print 'Login.'
    payload = {'username': bonita_username,
               'password': boita_password, 'redirect': 'false'}
    r = session.post(bonita_url + LOGIN_URL, data=payload)
    # Return if login failed
    if r.status_code != 200:
        print r
        return
    cookie = session.cookies.get_dict()

    # Search inactive users.
    print 'Search users.'
    payload = {'d': str()}
    r = session.get(bonita_url + USER_URL, params=payload, cookies=cookie)
    users = r.json()
    # Get inactive users if not clean all user.
    if not all:
        users = [x for x in users if x['enabled'] == 'false']

    # Delete inactive users.
    print 'Delete inactive users.'
    for user in users:
        print 'Username: ' + user['userName']
        r = session.delete(bonita_url + USER_URL + '/' +
                           user['id'], cookies=cookie)
    # Logout.
    print 'Logout.'
    r = requests.post(bonita_url + LOGOUT_URL)
