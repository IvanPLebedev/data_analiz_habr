import pandas as pd
import numpy as np 
import pycountry
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from yandex_translate import YandexTranslate
from yandex_translate import YandexTranslateException

import auxiliary_function as myfuncs

YANDEX_API_KEY = "trnsl.1.1.20191112T191006Z.7bd4f3ab17167843.ccf95966a99dd856b4823bc8d5a32af0d01630ee"
PLOT_LABEL_FONT_SIZE = 14
try:
    translate_obj = YandexTranslate(YANDEX_API_KEY)
except YandexTranslateException:
    translate_obj = None

def translate(string, translator_obj = None):
    if translator_obj == None:
        return string
    t = translate_obj.translate(string, 'en-ru')
    return t['text'][0]

def getColors(n):
    COLORS = []
    cm = plt.cm.get_cmap('hsv', n)
    for i in np.arange(n):
        COLORS.append(cm(i))
    return COLORS

def dict_sort(my_dict):
    keys = []
    values = []
    my_dict = sorted(my_dict.items(), key=lambda x:x[1], reverse=True)
    for k, v in my_dict:
        keys.append(k)
        values.append(v)
    return (keys,values)

df = pd.read_csv('./scrubbed.csv', escapechar='`', low_memory=False)
df = df.replace({'shape':None}, 'unknown')
country_label_count = pd.value_counts(df['country'].values) # Получить из таблицы список всех меток country с их количеством
for label in list(country_label_count.keys()):
    c = pycountry.countries.get(alpha_2=str(label).upper()) # Перевести код страны в полное название
    t = translate(c.name, translate_obj) # Перевести название страны на русский язык
    df = df.replace({'country':str(label)}, t)
    
shapes_label_count = pd.value_counts(df['shape'].values)
for label in list(shapes_label_count.keys()):
    t = translate(str(label), translate_obj) # Перевести название формы объекта на русский язык
    df = df.replace({'shape':str(label)}, t)