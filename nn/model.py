import random
import sqlite3
import time
from web.db import searching_popular_good_by_generic
import gensim
from scipy.spatial.distance import cosine

start_time = time.time()
path_to_model = 'nn/models/trained_nn1.model'
model = gensim.models.Word2Vec.load(path_to_model)
dict = {80:['Атероклефит', 'Триамцинолон', 'Солифенацин'], 321:['Панкреатин']}
conn = sqlite3.connect("web/cluster.db", check_same_thread=False)


def get_generics_recommndation(cheque):
    cursor = conn.cursor()

    # словарь кластер -> дженерики => кластер -> векоторы.
    def gen_to_vector(dict):
        clust_array = []
        d = {}
        for i in dict:
            for j in dict[i]:
                clust_array.append(list(model.wv.word_vec(j)))
            d[i] = clust_array
            clust_array = []
        return d  # Сделать


    def middleVector(args):
        mas = []
        for x in range(len(args[0])):
            mas.append(0)
        for vector in args:
            for x in range(len(vector)):
                mas[x] = mas[x] + vector[x]
        for x in range(len(mas)):
            mas[x] = mas[x] / len(args)
        return mas


    def searching_recommendation(clusterNum, generic_arr):
        sql = f"SELECT generic FROM generic_cluster WHERE cluster = '" + \
            str(clusterNum) + \
            f"' AND generic NOT IN ({','.join(['?']*len(generic_arr))})"
        cluster = cursor.execute(sql, generic_arr).fetchall()
        return [gen[0] for gen in cluster]


    vectors = gen_to_vector(cheque)
    for i in vectors:
        vectors[i] = middleVector(vectors[i])
    generics_rec = {}
    for i in cheque:
        generics_rec[i] = searching_recommendation(i, cheque[i])

    similarity_dict = {}
    for i in vectors:
        similarity_temp = {}
        for j in generics_rec[i]:
            similarity_temp[j] = cosine(vectors[i], model.wv.get_vector(j))
        similarity_dict[i] = sorted(similarity_temp.items(), key=lambda x: x[1])
        pass

    def get_rid_of_none(similarity_dict):
        similarity_temp = similarity_dict
        similarity_dict = {}
        for i in similarity_temp:
            if not similarity_temp[i] == []:
                similarity_dict[i] = similarity_temp[i]
        return similarity_dict
    similarity_dict = get_rid_of_none(similarity_dict)
    recomendating_gens = []
    for _ in range(5):
        if len(similarity_dict) == 0:
            break
        cluster = random.randint(0, len(similarity_dict)-1)
        keys = list(similarity_dict.keys())
        recomendating_gens.append(similarity_dict[keys[cluster]][0][0])
        similarity_dict[keys[cluster]]=similarity_dict[keys[cluster]][1:]
        similarity_dict = get_rid_of_none(similarity_dict)

    if len(recomendating_gens) > 0 and len(recomendating_gens)<5:
        additional = [i[0] for i in model.most_similar(recomendating_gens[0])[:5-len(recomendating_gens)]]
        recomendating_gens = recomendating_gens+additional
    recomendating_gens = []
    if len(recomendating_gens) == 0:
        recomendating_gens = [i[0] for i in model.most_similar(list(cheque.items())[0][1][0])[:5]]
    return recomendating_gens


def get_recs_from_gens(generics):
    recs = []
    for g in generics:
        temp = searching_popular_good_by_generic(g)
        recs.append(temp)
    return recs
