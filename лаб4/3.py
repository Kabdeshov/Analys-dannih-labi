'''
Вам нужно взломать пароль. Вам известно, что длина пароля не больше N.
и он может состоять только из цифр(0-9) и заглавных букв английского
алфавита(A-Z). Сколько возможных вариантов паролей может быть?
Какова вероятность взломать пароль с первой попытки.
'''

numLength = 10
alphabetLength = 26
n = int(input("Length of password: "))

casesAmount = (numLength + alphabetLength) ** n
print("Amount of possible password cases: %s" % casesAmount)
print("Probability of cracking password on the first try: %s%%" % (1 / casesAmount * 100))
