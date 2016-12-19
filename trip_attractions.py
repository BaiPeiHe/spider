
###
##  抓取 猫途鹰 景点的图片 标题 标签
#


from bs4 import BeautifulSoup
import requests

url = 'http://www.tripadvisor.cn/Attractions-g60763-Activities-oa30-New_York_City_New_York.html'

web_data = requests.get(url)

soup = BeautifulSoup(web_data.text,'lxml')

# a[target="_blank"] 是为了将带数字的标题过滤掉
titles = soup.select('div.property_title > a[target="_blank"]')
# img[width=160] 也是通过图片的特征 将多个图片 过滤掉
imgs = soup.select('img[width=160]')

cates = soup.select('div.p13n_reasoning_v2')


for title,img,cate in zip(titles,imgs,cates):

    data = {
        'title':title.get_text(),
        'img': img.get('src'),
        'cate':list(cate.stripped_strings),
    }
    print(data)
