# here will be database settings
import sqlite3
import random 

goods_on_one_page = 20
conn = sqlite3.connect("web/prd.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("SELECT count(*) FROM data;")
n_of_goods = cursor.fetchone()[0]


class Good(object):
    
    def __init__(self, query):
        self.pk = query[0]
        self.mnn = query[11]
        self.name = ' '.join(query[1].split()[:3])
        self.price = random.randint(317, 2000)


def get_page_goods(n_page):
    # we must get [n_page * 20 : (n_page + 1) * 20]
    cursor = conn.cursor()
    n_page -= 1
    offset = (n_page + 1) * goods_on_one_page
    print(offset, goods_on_one_page)
    cursor.execute(
        "SELECT * FROM data LIMIT {} OFFSET {};".format(goods_on_one_page, offset))
    goods = []
    queries = cursor.fetchall()
    for query in queries:
        g = Good(query)
        goods.append(g)
    return goods


def get_goods_by_ids(ids_list: list) -> list:
    cursor = conn.cursor()
    goods = []
    for i in ids_list:
        sql = "SELECT * FROM data WHERE id={};".format(i)
        cursor.execute(sql)
        query = cursor.fetchone()
        g = Good(query)
        goods.append(g)
    return goods


def get_n_most_popular(n):
    cursor = conn.cursor()
    goods = []
    sql = "SELECT * FROM data ORDER BY RANDOM() LIMIT {};".format(n)
    print(sql)
    cursor.execute(sql)
    queryies = cursor.fetchall()
    for query in queryies:
        goods.append(Good(query))
    return goods
