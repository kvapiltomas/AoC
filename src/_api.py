import requests
from os.path import exists

def get_session_id(filename):
    with open(filename) as f:
        return f.read().strip()

def get_url(day, year):
    return f'https://adventofcode.com/{YEAR}/day/{day}/input'

YEAR = 2022
DAY = 1
SESSION_ID_FILE = "session.cookie"
SESSION = get_session_id(SESSION_ID_FILE)
HEADERS = {
    "User-Agent": "https://github.com/kvapiltomas/AoC" 
}
COOKIES = {"session":SESSION}

CURPATH = os.path.abspath(os.curdir)

def get_input(day):
    path = f'{curpath}/2022/inputs/{day:02d}'
    
    if not exists(path):
        url = get_url(DAY, YEAR)
        r = requests.get(url, headers=HEADERS, cookies=COOKIES)
        if not r.ok:
            raise RuntimeError(f'Request failed with status: {r.status_code}')
        with open(path, 'w') as f:
            f.write(r.text[:-1])
    with open(path, 'r') as f:
        return f.read()