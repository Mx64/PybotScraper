import re
import requests
import user_agent
import datetime


def main():
    with open('./out/Pass_{date}.txt'.format(date=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")), 'w+') as f:
        for entry in filter(None, [reqRobots(host) for host in [line.strip() for line in open("./hosts", 'r')]]):
            f.write(entry)

    exit(1)


def reqRobots(_URL):
    _HEAD = {
        "user-agent": user_agent.generate_user_agent()
    }  # Add custom header to request
    if(re.match(r'^https?://', _URL) is None):
        _URL = '{PROTO}{URL}'.format(PROTO='https://', URL=_URL)
    _URL += '/robots.txt'

    _RESP = requests.get(_URL, headers=_HEAD)

    if(_RESP.status_code != 200):
        pass
    else:
        return createEntry(_URL, _RESP.text)


def createEntry(URL, CONTENT):
    if(CONTENT is None):
        pass
    else:
        return '{PREFIX}{CONTENT}{SUFFIX}' \
            .format(PREFIX='\n\nORIGIN: ' + URL + '\n\n', CONTENT=CONTENT, SUFFIX='\n\n' + 100*'=')


main()
