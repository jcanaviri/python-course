import urllib
from urllib.request import urlopen

URL = 'https://www.globalmentoring.com.mx/recursos/GlobalMentoring.txt'
req = urllib.request.Request(
    URL,
    headers={
        'User-Agent': \
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

words_list = []

with urlopen(req) as msg:
    for line in msg:
        words_by_line = line.decode('utf-8').split()
        for word in words_by_line:
            words_list.append(word)
print(words_list)
