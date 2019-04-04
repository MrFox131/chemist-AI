from untested_nn import predict, get_dataset_1, get_dataset_2, get_dataset_3, train_nn_model, load_nn_model, get_all_generics, get_val_all_unique_generics
import gensim
import random
# Neural networks
def test_nn_1(sentences,load = False): # Neural by Anodev TESTS ON DATASET_1: Success cases:270 Time 13 seconds
    if load == False:
        generics = get_all_generics()
        model = gensim.models.Word2Vec(sentences, size=300, window=len(sentences), min_count=1, workers=4, sample=1e-3, sg=1, seed=5)
        model = train_nn_model(model, data=sentences, epochs=100)
        model.save('./models/trained_nn1.model')
        return model
    else:
        model = gensim.models.Word2Vec.load('./models/trained_nn1.model')
        model.train(sentences, total_examples=len(sentences), epochs=100)
        return model

def test_nn_2(sentences, load = False):   # Neural by Anodev
    if load == False:
        generics = get_all_generics()
        val_gen = get_val_all_unique_generics()
        model = gensim.models.Word2Vec(generics, size=val_gen, window=100, min_count=1, workers=4, sample=1e-3)
        model.train(sentences, total_examples=len(sentences), epochs=10)
        vocab = list(model.wv.vocab.keys())
        model.train(vocab, total_examples=len(vocab), epochs=10)
        model.save('./models/trained_nn2.model')
        return model
    else:
        model = gensim.models.Word2Vec.load('./models/trained_nn2.model')
        model.train(sentences, total_examples=len(sentences), epochs=100)
        return model

def test_nn_3(sentences, load = False):
    if load == False:
        model = gensim.models.Word2Vec(sentences, size=50, window=len(sentences) , min_count=1)
        model = train_nn_model(model, data=sentences, epochs=10)
        model.save('./models/trained_nn3.model')
        return model
    else:
        model = gensim.models.Word2Vec.load('./models/trained_nn3.model')
        model.train(sentences, total_examples=len(sentences), epochs=100)
        return model

def test_nn_4(sentences, load = False): # Neural by Gargulia TESTS on Dataset_1: Success cases: 60
    if load == False:
        val_generics = get_val_all_unique_generics()
        model = gensim.models.Word2Vec(sentences, size=val_generics, window=10, workers=4, min_count=1)
        model.train(sentences, total_examples=len(sentences), epochs=10)
        model.save('./models/trained_nn4.model')
        return model
    else:
        model = gensim.models.Word2Vec.load('./models/trained_nn4.model')
        model.train(sentences, total_examples=len(sentences), epochs=100)
        return model

def test_nn_5(sentences, load = False):
    if load == False:
        model = gensim.models.Word2Vec(sentences, size=50, window=len(sentences) , min_count=1, sorted_vocab=0)
        model = train_nn_model(model, data=sentences, epochs=50)
        model.save('./models/trained_nn5.model')
        return model
    else:
        model = gensim.models.Word2Vec.load('./models/trained_nn5.model')
        model.train(sentences, total_examples=len(sentences), epochs=100)
        return model
##################CONFIG##################################
sentences = get_dataset_1() # or get_dataset_2() or get_dataset_3()
model = test_nn_1(sentences, load=False) # choose neural to test
TEST_LOO = True
TEST_VECT_DIST = False
########FOR VECT_DIST_TEST################################
w1 = 'Парацетамол' # Word 1
w2 = 'Фозиноприл' # Word
##########################################################
if TEST_LOO:
    n_test_cases = 0
    n_succ_cases = 0
    n_fail_cases = 0
    sentences = get_dataset_1() #CHANGE
    for s in sentences:
        if len(s) > 2:
            n_test_cases += 1
            item_we_need = s.pop(random.randint(0, len(s) - 1))
            predictions = [i[0] for i in predict(s, model)]
            if item_we_need in predictions:
                    n_succ_cases += 1
            else:
                    n_fail_cases += 1


    print("All cases: {}".format(n_test_cases))
    print("Success cases: {}".format(n_succ_cases))
    print("Failed cases: {}".format(n_fail_cases))
elif TEST_VECT_DIST:
    model = test_nn_1(sentences)
    print('Новая 1 н.:', model.wv.similarity(w1, w2))
    model = test_nn_2(sentences)
    print('Новая 2 н.:', model.wv.similarity(w1, w2))
    model = test_nn_3(sentences)
    print('Новая 3 н.:', model.wv.similarity(w1, w2))
    model = test_nn_4(sentences)
    print('Новая 4 н.:', model.wv.similarity(w1, w2))
    model = test_nn_5(sentences)
    print('Новая 5 н.:', model.wv.similarity(w1, w2)) # Add other neural network by following this syntax!