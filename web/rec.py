from . import db
from nn.model import predict


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
    print(cluster_generics)
    # Надо передать словарь номер кластеров: массивов дженериков, сгруппированных по кластерам


