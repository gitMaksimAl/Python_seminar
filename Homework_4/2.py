# -*- coding: utf-8 -*-

# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой
# грядке, причем кусты высажены только по окружности. Таким образом, у каждого
# куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты
# обладают разной урожайностью, поэтому ко времени сбора на них выросло
# различное число ягод – на i-ом кусте выросло ai ягод. В этом фермерском
# хозяйстве внедрена система автоматического сбора черники. Эта система состоит
# из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за
# один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с
# этого куста и с двух соседних с ним. Напишите программу для нахождения
# максимального числа ягод, которое может собрать за один заход собирающий
# модуль, находясь перед некоторым кустом заданной во входном файле грядки.

n = int(input('Сколько кустов? '))
garden_bed = [int(input(f'Ягод на {i + 1} кусте ')) for i in range(n)]

print(*garden_bed)
max_fee = garden_bed[-1] + garden_bed[0] + garden_bed[1]
for i in range(1, n):
    fee = garden_bed[i - 1] + garden_bed[i % n] + garden_bed[(i + 1) % n]
    if fee > max_fee:
        max_fee = fee

print(max_fee)
