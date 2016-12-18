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


'''

<a href="/Attractions-g60763-Activities-c42-t204-New_York_City_New_York.html" data-params="bjhNXy9BdHRyYWN0aW9ucy1nNjA3NjMtQWN0aXZpdGllcy1jNDItdDIwNC1OZXdfWW9ya19DaXR5X05ld19Zb3JrLmh0bWxfcGVB" onclick="ta.servlet.Attractions.narrow.setEvtCookieWrapper('Attraction_List_Click', 'Rollup_click', 'name', 4, 'QXkxXy9BdHRyYWN0aW9ucy1nNjA3NjMtQWN0aXZpdGllcy1jNDItdDIwNC1OZXdfWW9ya19DaXR5X05ld19Zb3JrLmh0bWxfRkIz'); ta.call('ta.servlet.Attractions.narrow.ajaxifyLink', event, this)">美食游览 (42)</a>


<a href="/Attraction_Review-g60763-d136028-Reviews-Lincoln_Center_for_the_Performing_Arts-New_York_City_New_York.html" onclick="ta.setEvtCookie('Attraction_List_Click', 'POI_click', 'name', 5, '/Attraction_Review')" target="_blank">林肯表演艺术中心</a>


<img alt="林肯表演艺术中心" width="160" style="height: 160px; width: 160px;" id="lazyload_548736566_5" class="photo_image" height="160" src="http://ccm.ddcdn.com/ext/photo-l/01/7f/7e/a5/lincoln-center.jpg">

'''