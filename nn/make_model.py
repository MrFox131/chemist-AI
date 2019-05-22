# -*- coding: utf8 -*-
# Имя: make_model.py
# Месторасположение файла: ProjectRoot/nn/
# Автор скрипта: Anodev (OPHoperHPO)
# Описание скрипта:
#     Этот скрипт создает натренерованную модель из датасета!
#     В последствии данная модель используется рек. системой!
#     Сама модель по завершении работы скрипта будет лежать по пути ./models/trained_nn1.model.
#     Данный скрипт зависит от файла functions.py!
#     Он импортирует от туда функции получения различных датасетов и фун-ю тренеровки модели!


# Зависимости
# Локальные зав-сти
from functions import get_dataset_1  # 1000 чеков! Не требует никаких доп. файлов!
from functions import get_dataset_2  # 1500000 чеков! Требует файл ./data/databases/train_dataset2.db
from functions import get_dataset_3  # 1500000 чеков разбитых по парам! Требует файл /data/databases/train_dataset3.db
from functions import get_all_generics  # Все generic из базы продуктов! Требует файл /data/databases/generics.db
from functions import get_val_all_unique_generics  # Кол-во УНИКАЛЬНЫХ generic из базы продуктов Требует файл /data/databases/generics.db
from functions import train_nn_model  # Фун-я тренеровки модели
# Загружаемые зав-сти
import gensim # Word2vec модуль
import time # Время работы скрипта

# Функции
def test_nn_1(sentences, load=False):  # Neural by Anodev TESTS ON DATASET_1: Success cases:270 Time 13 seconds
    if load == False:
        generics = get_all_generics()
        model = gensim.models.Word2Vec(sentences, size=300, window=len(sentences), min_count=1, workers=4, sample=1e-3,
                                       sg=1, seed=5)
        model = train_nn_model(model, data=sentences, epochs=100)
        model.save('./models/trained_nn1.model')
        return model
    else:
        model = gensim.models.Word2Vec.load('./models/trained_nn1.model')
        model.train(sentences, total_examples=len(sentences), epochs=100)
        return model


# Настройка скрипта
start_time = time.time() # Необходимая переменная для рассчёта времени работы скрипта!
sentences = get_dataset_1()  # или get_dataset_2() или get_dataset_3()
model = test_nn_1(sentences, load=False)  # Выберите нейросеть, если указали их несколько!

print('Скрипт завершил свою работу! Файл модели лежит по пути ./models/trained_nn1.model. ',
      'Время работы скрипта: %s секунд' % (time.time() - start_time))