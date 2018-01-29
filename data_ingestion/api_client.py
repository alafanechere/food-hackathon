import requests
import datetime
import time
TOKEN_ENDPOINT = 'https://api.prognolite.com/1.0/oauth/access_token.json'
TRANSACTION_ENDPOINT = 'https://api.prognolite.com/1.0/cashier_transaction_positions/get/2/?format=json'
# 2 Baechi one
# 3 Juckerhof one
def get_token():
    body = {
        'grant_type': 'password',
        'client_id':  '',
        'client_secret': '',
        'username': '',
        'password': ''
    }

    r = requests.post(TOKEN_ENDPOINT, data=body)
    return r.json()

def get_transactions(token):
    now = datetime.datetime.now()
    last_thirty_minutes = now - datetime.timedelta(minutes=30)

    now_posix = int(time.mktime(now.timetuple()))
    last_posix = int(time.mktime(last_thirty_minutes.timetuple()))

    print(now_posix)
    print(last_posix)
    r = requests.get(TRANSACTION_ENDPOINT, params={
    'format': 'json',
    'start': now_posix,
    'from': last_posix}, headers={'Authorization': f'Bearer {token}'})
    print(r.text)
    return r.json()

if __name__ == '__main__':
    token = get_token()
    print(get_transactions(token))
