import requests
from lxml import html

url = "http://www.dolarhoje.com/"

r = requests.get(url)
dom = html.fromstring(r.text)
dolar_em_real = dom.xpath("//*[@id='nacional']")
print(dolar_em_real[0].value)
