# -*- coding; utf-8 -*-

# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

S = int(input('Сколько всего было сделано журавликов '))

# x - boy_cranes -> (x + x) * 2 + (x + x) = S -> 6x = S
boy_cranes = S // 6
# katja_cranes = (x + x) * 2 -> 4x
katja_cranes = boy_cranes * 4
in_process = S - (katja_cranes + int(boy_cranes) * 2)

if in_process:
    print('Вы не правильно посчитали журавликов!!!')
else:
    print(f'Катя сделала {katja_cranes} журавликов, остальные сделали по {int(boy_cranes)}.')
