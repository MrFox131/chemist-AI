from . import db
from nn.model import get_generics_recommndation, get_recs_from_gens


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
    recs = get_recs_from_gens(get_generics_recommndation(cluster_generics))
    print(recs)
    return recs
    # Надо передать словарь номер кластеров: массивов дженериков, сгруппированных по кластерам
