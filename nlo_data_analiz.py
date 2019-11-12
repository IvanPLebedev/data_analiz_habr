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


