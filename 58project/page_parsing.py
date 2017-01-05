from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
ceshi = client.ceshi
url_list = ceshi.url_list3
item_info = ceshi.item_info3

# spider 1


# 获得当前分类中:商品的 url
def get_links_from(channel,pages,who_sells=0):
    # http://bj.58.com/diannao/0/pn3
    list_view = '{}{}/pn{}'.format(channel,str(who_sells),str(pages))
    wb_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text,'lxml')
    if soup.find('td','t'):

        for link in soup.select('td.t a.t'):
            item_link = link.get('href').split('?')[0]
            url_list.insert_one({'url' : item_link})

            print(item_link)
    else:
        pass

    #Nothing !


# 获取每一个商品的简单信息
def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text , 'lxml')

    title = soup.title.text

    # 判断网址是否为 404
    no_longer_exist = '404' in title
    if no_longer_exist:
        print('\n\n\n\n  404  \n\n\n\n')
        pass
    else:

        # 价格
        price = soup.select('span.price_now')[0].text if soup.find_all('span','price_now') else None
        price_now = ''
        price_ori = ''
        if price != None:
            price_now = soup.select('span.price_now > i')[0].text + '元'
            if '原价' in price:
                price_ori = price.split('：')[2]
            else:
                price_ori = '无'

        # 地址
        area = soup.select('div.palce_li > span > i')[0].text if soup.find_all('span','price_now') else None

        # 标签
        tags = list(soup.select('div.biaoqian_li > span')) if soup.find_all('span','price_now') else None
        final_tags = []
        if tags != None:
            for tag in tags:
                final_tags.append(tag.get_text())


    item_info.insert_one({'title':title,'price':price,'area':area,'tag':final_tags})
    print({'title':title,'price_now':price_now,'price_ori':price_ori,'area':area,'tag':final_tags})


#  转转
# 有原价
get_item_info('http://zhuanzhuan.58.com/detail/799547182400176135z.shtml')

# 无原价
# get_item_info('http://zhuanzhuan.58.com/detail/816976264910028804z.shtml')

# 58同城
# get_item_info('http://bj.58.com/diannao/26673106474551x.shtml')