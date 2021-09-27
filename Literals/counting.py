import urllib
from urllib.request import urlopen

URL = 'https://www.globalmentoring.com.mx/recursos/GlobalMentoring.txt'
req = urllib.request.Request(
    URL,
    headers={
        'User-Agent': \
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

with urlopen(req) as msg:
    content = msg.read().decode('utf-8')

print(content.count('Universidad'))

print('python' in content.lower())

print(content.startswith('En'))
print(content.endswith('mx'))
