from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.tmd.go.th/weather/province/samut-prakan'

webopen = urlopen(url)
html_page = webopen.read()
webopen.close()

data = BeautifulSoup(html_page,'html.parser')

print(data.prettify())

