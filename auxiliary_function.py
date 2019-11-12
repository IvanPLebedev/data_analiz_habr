import matplotlib.pyplot as plt
import numpy as np 
# генерация цветовых схем
# возвращает список цветов
def getColors(n):
    COLORS = []
    cm = plt.cm.get_cmap('hsv', n)
    for i in np.arange(n):
        COLORS.append(cm(i))
    return COLORS