
from bs4 import BeautifulSoup
import requests

header = {
    'User-Agent' :'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}

url = 'http://www.tripadvisor.cn/Attractions-g60763-Activities-oa30-New_York_City_New_York.html'

mb_data = requests.get(url,headers=header)

soup = BeautifulSoup(mb_data.text,'lxml')

imgs = soup.select('div.thumb.thumbLLR.soThumb > img')

for i in imgs:
    print(i.get('src'))
    print(i)