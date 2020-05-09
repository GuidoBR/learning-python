# -*- coding: utf-8 -*-
import requests
import subprocess
from lxml import html

url = "http://www.dolarhoje.com/"

r = requests.get(url)
dom = html.fromstring(r.text)
dolar_em_real = dom.xpath("//*[@id='nacional']")[0].value
subprocess.Popen(['notify-send', 'Dólar hoje vale: R$ %s' % str(dolar_em_real)])
