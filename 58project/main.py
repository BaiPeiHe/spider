from multiprocessing import Pool
from channel_extract import chenel_list
from page_parsing import get_links_from


def get_all_links_from(channel):

    for num in range(1,101):
        get_links_from(channel,num)




if __name__ == '__main__':
    # 进程池
    # processes 是设置开启多少个进程,并不是进程越多效率越高,建议让他自动分配
    # pool = Pool(processes=4)
    pool = Pool()
    # map 函数: 将参数2 依次的一个个的放在参数1中,运行
    pool.map(get_all_links_from,chenel_list.split())


