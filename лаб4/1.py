'''
Напишите программу, которая подбрасывает монетку с вероятностью
выпадения орла 70%, соответственно вероятность выпадения решки 30%.
Проделайте 1000 таких бросков и сделайте наглядный график
(python: matplotlib).
'''

import random
import matplotlib as lib
import matplotlib.pyplot as plot

tossings = []

for i in range(1, 1001):
    rand = random.randint(1, 100)
    if (rand >= 30):
        tossings.append(0) # орел
    else:
        tossings.append(1) # решка

labels = ['Eagles', 'Tails']
values = [0] * 2

for i in range(len(tossings)):
    if (tossings[i] == 0):
        values[0] += 1
    else:
        values[1] += 1

figure1, ax1 = plot.subplots()
ax1.pie(values, labels = labels,
        autopct = '%1.1f%%', shadow = True, startangle = 90)
ax1.axis('equal')
plot.show()
