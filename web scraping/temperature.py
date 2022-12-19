from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.tmd.go.th/weather/province/samut-prakan'

webopen = urlopen(url)
html_page = webopen.read()
webopen.close()

data = BeautifulSoup(html_page,'html.parser')

temp = data.find('h2',{'class' : 'txt_temp'})
tital = data.find('h1',{'class' : 'text-dark1'})
print(tital.text)
print(temp.text)

