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


def LD(s,t):
    s = ' ' + s
    t = ' ' + t
    d = {}
    S = len(s)
    T = len(t)
    for i in range(S):
        d[i, 0] = i
    for j in range (T):
        d[0, j] = j
    for j in range(1,T):
        for i in range(1,S):
            if s[i] == t[j]:
                d[i, j] = d[i-1, j-1]
            else:
                d[i, j] = min(d[i-1, j], d[i, j-1], d[i-1, j-1]) + 1
    return d[S-1, T-1]


def find_items(request):
    cursor = conn.cursor()

    query = "SELECT * FROM 'data' WHERE Наименование LIKE '%" + str(request)[0].upper() + str(request)[1:len(
        str(request))].lower() + "%' LIMIT 20;"
    queryResult = cursor.execute(query)
    resultsAmount = len(list(queryResult))
    allResults = []

    if resultsAmount == 0:
        for i in range(min(10, len(request))):
            query = "SELECT * FROM 'data' WHERE Наименование LIKE '%" + str(request[0:i]) + "%" + str(request[(i + 1):len(request)]) + "%' LIMIT 20;"
            queryResult = cursor.execute(query)
            data = queryResult.fetchall()
            allResults += data

    goods = []
    for query in allResults:
        g = Good(query)
        print(LD(' '.join(g.name.split()[:1]), ' '.join(request.split()[:1])))
        if LD(' '.join(g.name.split()[:1]), ' '.join(request.split()[:1])) < 5:
            goods.append(g)
    return goods


def get_page_goods(n_page):
    # we must get [n_page * 20 : (n_page + 1) * 20]
    cursor = conn.cursor()
    n_page -= 1
    offset = (n_page + 1) * goods_on_one_page
    cursor.execute(
        "SELECT * FROM data LIMIT {} OFFSET {};".format(
            goods_on_one_page, offset
        ))
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
        sql = "SELECT * FROM data WHERE id='{}';".format(i)
        cursor.execute(sql)
        query = cursor.fetchone()
        g = Good(query)
        goods.append(g)
    return goods


def get_n_most_popular(n):
    cursor = conn.cursor()
    goods = []
    sql = "SELECT * FROM data ORDER BY RANDOM() LIMIT {};".format(n)
    cursor.execute(sql)
    queryies = cursor.fetchall()
    for query in queryies:
        goods.append(Good(query))
    return goods
