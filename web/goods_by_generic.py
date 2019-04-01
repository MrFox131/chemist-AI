import sqlite3
import random

conn = sqlite3.connect("web/good-generic.db")
cursor = conn.cursor()


def searching_popular_goods_by_generic(gen):
    sql = "SELECT good, count(generic) as cnt from good_generic where generic = '"+gen+"' group by good order by cnt DESC limit 5"
    smth = [i[0] for i in sorted(cursor.execute(sql).fetchall(), key=lambda x:x[1]*random.random()/302366)]
    return smth[0]
