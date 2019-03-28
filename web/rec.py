from db import get_goods_by_ids


n_of_goods_we_recommend = 5


def get_recs_by_goods_ids(busk_items_ids: list) -> list:
    '''return 5 items we our rec system recommends'''
    '''right now code just returns 5 Lisobacts'''
    goods = []
    get_goods_by_ids(busk_items_ids)
    return goods
