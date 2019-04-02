import gensim
generics = [['Панкреатин', 'Фозиноприл', 'Панкреатин'], ['Панкреатин']]


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


print(genCLStoVecCLS(generics, path_to_model = './models/trained_nn1.model'))
