import time
import requests

password = 'mnnkR8TewKdsf9nEwRBFkNvzAQJceTkBWrgchXVjjna7u2jKejKLfKmnx2Cgsc5C'

while True:
    r = requests.get('https://abb.cristianlivella.com/get.php', auth=('abb', password), verify=False)
    if r.status_code is 200:
        if r.text is not '0':
            requests.get('http://192.168.4.1/pos' + r.text)
            print(r.text)
    else:
        print('Error server')
    time.sleep(0.2)
