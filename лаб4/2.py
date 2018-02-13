'''
В ящике лежат N красных и M синих шаров.
Какова вероятность вытащить из ящика красный шар?
Какова вероятность вытащить синий шар?
N и M задаются через консоль (в python: input() ) .
Ответ вывести через пробел в консоле.
'''

n = int(input("N = "))
m = int(input("M = "))

print("Probability of getting a red ball: %s%%" % (n / (n + m) * 100))
print("Probability of getting a blue ball: %s%%" % (m / (n + m) * 100))
