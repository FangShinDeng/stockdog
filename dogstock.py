import requests
import re

StockNo = 4956
url = "https://www.stockdog.com.tw/stockdog/index.php?m=overview&sid="+ format(StockNo)
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

rs = requests.session()
res = rs.get(url,headers = headers)
m = re.findall('document.getElementById\(\'g\d+\'\).innerHTML=\'<iframe src=\"(.*?)\"', res.text)
# print(m[0])
res2 = rs.get("https://www.stockdog.com.tw/stockdog/" + m[0], headers = headers)
print(res2.text)

for url in m:
    print("https://www.stockdog.com.tw/stockdog/" +url)
    pass

f = open('index.html', 'w+', encoding= "utf-8")
f.write(res.text)
f.close()
