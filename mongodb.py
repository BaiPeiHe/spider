from pymongo import MongoClient

# 数据库

client = MongoClient('localhost',27017)
walden = client.walden
sheet_tab = walden['sheet_tab']


# 打开文件,并将数据写入数据库

def fileDB_write_in_DB:

    path = '/Users/baihe/Code/Python/spider/walden.txt'
    with open(path, 'r') as f:
        lines = f.readlines()
        for index, line in enumerate(lines):
            data = {
                'index': index,
                'line': line,
                'words': len(line.split())
            }
            sheet_tab.insert_one(data)


# $lt / $lte / $gt / $gte / $ne 依次等价于< , <= , > , >= ,!= (l 表示 less ,t 表示 than, g 表示 greater, e 表示 equal, n 表示 not)
# {'words':{'$lt':5}} 表示 当 words 对应的值小于5

def select_data:
    for item in sheet_tab.find({'words': {'$lt': 5}}):
        print(item['line'])