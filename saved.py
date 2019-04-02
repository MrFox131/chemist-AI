import sqlite3
import gensim
path_to_model = './models/trained_nn1.model'
model = gensim.models.Word2Vec.load(path_to_model)
dict = {80:['Атероклефит', 'Триамцинолон', 'Солифенацин'], 321:['Панкреатин']}
generics = [['Панкреатин', 'Фозиноприл', 'Панкреатин'], ['Панкреатин']]
conn = sqlite3.connect("/home/anodev/PycharmProjects/neur/nn/data/databases/gen-clusters.db")
cursor = conn.cursor()

def genCLStoVecCLS(dict):
    clust_array = []
    d = {}
    for i in dict:
        for j in dict[i]:
            clust_array.append(list(model.wv.word_vec(j)))
        d[i]=clust_array
        clust_array=[]
    return d # Сделать

def Bridge1(num, dict):
    return dict[num] ### Переделать
def middleVector( args ):
    mas = []
    for x in range(len(args[0])):
        mas.append(0)
    for vector in args:
        for x in range(len(vector)):
            mas[x] = mas[x] + vector[x]
    for x in range(len(mas)):
        mas[x] = mas[x] / len(args)
    return mas

def searching_recommendation(clusterNum, generics_arr, vector):
    for generic_arr in generics_arr:
        sql = f"SELECT generic FROM generic_cluster WHERE cluster = '"+str(clusterNum)+f"' AND generic NOT IN ({','.join(['?']*len(generic_arr))})"
        cluster = cursor.execute(sql, generic_arr).fetchall()
        generics_from_arr = []
        for gen in cluster:
            generics_from_arr.append(str(str(str(str(gen).replace('(', '')).replace(')', '')).replace(',', '')).replace("'", ''))
        not_in_cart = set(generics_from_arr)
        in_cart = set(generic_arr)
        not_in_cart = list(not_in_cart.difference(in_cart))
        not_in_cart_vectors = []
        for k in not_in_cart:
            not_in_cart_vectors.append(model.wv.most_similar_to_given(vector, [fpr ])) # NOT WORK REPAIR!
    return 0 # Переделать
cluster = 80
vector = middleVector(Bridge1(cluster,genCLStoVecCLS(dict)))
print(searching_recommendation(cluster, dict.values(), vector))
#searching_recommendation(80, ['Альфакальцидол', 'Салициловая кислота', 'Активированный уголь', 'Флуконазол', 'Клотримазол'])
