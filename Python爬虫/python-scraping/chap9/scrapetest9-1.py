import requests

params = {'firstname': 'Huang', 'lastname': 'Hongfei'}
r = requests.post("http://pythonscraping.com/files/processing.php", data=params)