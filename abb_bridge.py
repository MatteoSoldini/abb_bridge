import time
import requests
requests.packages.urllib3.disable_warnings()

password = 'INSERT_PASSWORD_HERE'

print("Daemon started")
while True:
    try:
        try:
            r = requests.get('https://abb.cristianlivella.com/get.php', auth=('abb', password), verify=False, timeout=5)
        except:
            print("No response from server")
            continue
        if r.status_code == 200:
            if r.text != '0':
                print('Server say: ' + r.text)
                try:
                    requests.get('http://192.168.4.1/pos' + r.text, timeout=5)
                except:
                    print('No response from ESP')
            else:
                print('Server say nothing')
        else:
            print('Server error')
    except:
        print("Fatal error!")
    time.sleep(0.2)
