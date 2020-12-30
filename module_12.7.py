per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = float(input("Введите сумму которую Вы планирует положить под проценты: "))

deposit = []

for i in per_cent:
    deposit.append(per_cent[i]*money/100)

print("Максимальная сумма, которую вы можете заработать", max(deposit))

