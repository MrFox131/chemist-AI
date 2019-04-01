from . import db
from nn.untested_nn import predict


n_of_goods_we_recommend = 5


def get_recs_from_db(busk_items_ids: list, n_of_items: list) -> list:
    '''return 5 items we our rec system recommends'''
    '''right now code just returns 5 Lisobacts'''
    goods_names = [g.name for g in db.get_goods_by_ids(busk_items_ids)]
    if goods_names:
        try:
            predictions = predict(goods_names)
        except KeyError:
            predictions = []
        recs = [i[0] for i in predictions[:n_of_goods_we_recommend]]
        if len(recs) < 5:  # there are few no recs
            # HERE WE MUST RETURN MOST POPULAR
            recs = db.get_n_most_popular(n_of_goods_we_recommend)
    else:
        recs = db.get_n_most_popular(n_of_goods_we_recommend)
    return recs
