#checks wikipedia for available usernames
import requests,json
users=[]
for user in users:
    c=requests.post(f'https://en.wikipedia.org/w/api.php?action=query&format=json&list=users&ususers={user}&usprop=cancreate&formatversion=2&errorformat=html&errorsuselocal=true&uselang=en', headers={'content-type':'application/json'})
    if json.loads(c.text)['query']['users'][0]['cancreate']:
        print(f'{user} not taken')
