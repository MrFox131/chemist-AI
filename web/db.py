# here will be database settings

goods_on_one_page = 3


class Good(object):
    name = 'Лизобакт'
    category = 'Антисептическое средство'
    price = 230

    def __init__(self, pk):
        self.pk = pk


def get_page_goods(n_page):
    # we must get [n_page * 20 : (n_page + 1) * 20]
    goods = []
    for i in range(1, goods_on_one_page + 1):
        g = Good(i)
        goods.append(g)
    return goods


def get_goods_by_ids(ids_list: list) -> list:
    goods = []
    for i in ids_list:
        g = Good(i)
        goods.append(g)
    return goods
