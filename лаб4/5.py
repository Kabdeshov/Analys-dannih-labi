'''
Вам дан текст на английском языке, посчитайте частоту встречаемости
каждой буквы, не учитывайте все другие знаки препинания и пробел
(буквы только a-z). Покажите наглядно на графике. Пример текста:
“hello, my friend. how do you do?”. Ответ в виде графика.
'''

import numpy as np
import matplotlib as lib
import matplotlib.pyplot as plot

content = input("Your string: ")
frequency = [0] * 256

for ch in list(content):
    valueOfChar = ord(ch)
    if (valueOfChar >= 97 and valueOfChar <= 122):
        frequency[valueOfChar] += 1

x = np.arange(26)
labels = []
for i in range(97, 123):
    labels.append(chr(i))
frequency = frequency[97 : 123]

fig, ax = plot.subplots()
plot.bar(x, frequency)
plot.xticks(x, labels)
plot.show()
