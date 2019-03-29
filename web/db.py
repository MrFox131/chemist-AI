# here will be database settings

goods_on_one_page = 20


class Good(object):
    name = 'Лизобакт'
    category = 'Антисептическое средство'
    price = 230

    def __init__(self, pk):
        self.pk = pk


def get_page_goods(n_page):
    # we must get [n_page * 20 : (n_page + 1) * 20]
    goods = []
    n_page -= 1
    for i in range(n_page * goods_on_one_page, (n_page + 1) * goods_on_one_page):
        g = Good(i)
        goods.append(g)
    return goods


def get_goods_by_ids(ids_list: list) -> list:
    goods = []
    for i in ids_list:
        g = Good(i)
        goods.append(g)
    return goods


def get_n_most_popular(n):
    goods = []
    for i in range(n):
        goods.append(Good(i))
    return goods
