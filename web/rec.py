from db import get_goods_by_ids, get_n_most_popular


n_of_goods_we_recommend = 5


def get_recs_from_db(busk_items_ids: list, n_of_items: list) -> list:
    '''return 5 items we our rec system recommends'''
    '''right now code just returns 5 Lisobacts'''
    goods = get_goods_by_ids(busk_items_ids)
    recs = []  # !!! HERE WE MUST ACTUALLY GET RECS
    if not recs:  # there are no recs
        # HERE WE MUST RETURN MOST POPULAR
        recs = get_n_most_popular(n_of_goods_we_recommend)
    return recs
