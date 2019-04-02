from . import db
from nn.untested_nn import predict


n_of_goods_we_recommend = 5


def get_recs_from_db(busk_items_ids: list, n_of_items: list) -> list:
    '''return 5 items we our rec system recommends'''
    goods = db.get_goods_by_ids(busk_items_ids)
    generics = [g.generic for g in goods]
    generics = list(set(generics))
    clusters = db.get_generics_clusters(generics)
    cluster_generics = {}
    for i in range(len(clusters)):
        print(clusters[i])
        if clusters[i] is not None:
            cluster_generics[clusters[i]] = cluster_generics.get(
                clusters[i],
                []
            ) + [generics[i]]
    generics_gb_clusters = list(cluster_generics.values())
    print(generics_gb_clusters)
    # Надо передать массив массивов дженериков, сгруппированных по кластерам


    # WE MUST DELETE THE FOLLOWING AND RECOMMEND ACCORDING TO CLUSTERS
    goods_names = [g.name for g in goods]
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
