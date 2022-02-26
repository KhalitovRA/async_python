from time import time


def gen_filename():
    '''поиграться в терминале и вспомнить python -i 3_generators.py'''
    while True:

        pattern = 'file-{}.jpeg'
        t = int(time() * 1000)

        yield pattern.format(str(t))

        sum = 234 + 245
        print(sum)


def gen1(s):
    for i in s:
        yield i


def gen2(n):
    for i in range(n):
        yield i


g1 = gen1('loll')
g2 = gen2(4)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)


    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass