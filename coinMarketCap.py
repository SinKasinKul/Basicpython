 #This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

#url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
#url = ' https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'10',
  'convert':'THB'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '0e92e347-0ed3-4725-8f42-c977da39f2b7',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)