age = 0
summ = 0

kol_bil = int(input("Здравствуйте! Какое количество билетов Вы хотите приобрести? "))

for i in range(1, kol_bil + 1):
    print("Укажите возраст", i, "посетителя: ")
    age = int(input())
    if 18 <= age <= 25:
        summ += 990
    elif age > 25:
        summ += 1390

print('Cумма к оплате: ', summ * 0.9 if kol_bil > 3 else summ)