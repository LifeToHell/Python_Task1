print('Задача 2: Найдите сумму цифр трехзначного числа.')


a = int(input('Введите трезначное  число: '))
a = int(abs(a))
if a < 999 and a >= 100:
    c = a//100 + a//10 % 10 + a % 10
    print(c)
else:
    print('Данное число не соответствует требованиям')



print('Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?')
s = int(input('Сколько журавликов сделали : '))
c = s/6
k = s/6*4
print(
    f'Катя сделала =   {round(k)}, Сережа сделал =  {round(c)}, Петя сделал =  {round(c)}')



print('Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.')
a = int(input('Введите шестизначное  число: '))
# вариант без использования массива
c = a//1000 % 10 + a//100000 + a//10000 % 10
b = a//100 % 10 + a//10 % 10 + a % 10
if c == b:
    print(f'Сумма первой стороный = {c}, сумма второй стороны = {b}, поздавлям! Ваш билетик счастливый')
else:
    print(f'Сумма первой стороный = {c}, сумма второй стороны = {b}, стороны не равны. Возможно вам повезет в другой раз.')


 
print('Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).')
a = int(input('Сколько плиток по оси x: '))
b = int(input('Сколько плиток по оси y: '))
s = int(input('Сколько плиток мы безжалостно хотим отделить от идеальной шоколадки: '))
if s < a * b and ((s % a == 0) or (s % b == 0)):
    print('Да, мы можем аккуратно надломить шоколадку')
else:
    print('Лучше не стоит этого делать, шоколадка на два прямоуголька не разломится.')

