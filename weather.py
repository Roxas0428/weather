import requests
from bs4 import BeautifulSoup
token="WmykvEOULYNUhiwVLnH3ZDqYC5EeaLZs0taZR71nky8"
url="https://notify-api.line.me/api/notify"
auth={"Authorization":"Bearer WmykvEOULYNUhiwVLnH3ZDqYC5EeaLZs0taZR71nky8"}
tenki_url="https://weather.yahoo.co.jp/weather/jp/1b/1400.html"
response=requests.get(tenki_url)
response.text
BeautifulSoup(response.text,"html.parser")
html=BeautifulSoup(response.text,"html.parser")
forecast=html.find_all("div",attrs={"class":"forecastCity"})[0]
tomorrow=forecast.find_all("div")[1]
weather=tomorrow.find_all("p",attrs={"class":"pict"})[0].text.replace("\n","").replace(" ","")
high=tomorrow.find_all("li")[0].text
low=tomorrow.find_all("li")[1].text
rain_06=tomorrow.find_all("td")[4].text
rain_0612=tomorrow.find_all("td")[5].text
rain_1218=tomorrow.find_all("td")[6].text
rain_1824=tomorrow.find_all("td")[7].text
message="""
明日の天気は{}
最高気温は{}
最低気温は{}
降水確率は
0-6時:{}
6-12時:{}
12-18時:{}
18-24時:{}
です""".format(weather,high,low,rain_06,rain_0612,rain_1218,rain_1824)
content={"message":message}
requests.post(url,headers=auth,data=content)


