import sqlite3

conn = sqlite3.connect("cluster.db")
cursor = conn.cursor()
def genCLStoVecCLS(generics, path_to_model = './models/trained_nn1.model'):
    model = gensim.models.Word2Vec.load(path_to_model)
    clust_array = []
    d = []
    for i in generics:
        for j in i:
            clust_array.append(list(model.wv.word_vec(j)))
        d.append(clust_array)
        clust_array=[]
    return d

def searching_recommendation(clusterNum, generic_arr, vector):
    sql = f"SELECT generic FROM generic_cluster WHERE cluster = '"+str(clusterNum)+f"' AND generic NOT IN ({','.join(['?']*len(generic_arr))})"
    cluster = cursor.execute(sql, generic_arr).fetchall()
    for gen in cluster:
        print(gen)
    print(cluster)
    return 0

searching_recommendation(80, ['Альфакальцидол', 'Салициловая кислота', 'Активированный уголь', 'Флуконазол', 'Клотримазол'])



