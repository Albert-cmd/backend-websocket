import requests

r = requests.get('http://192.168.1.108/CGI/command/snap?channel=0')

print(r)

