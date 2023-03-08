def zad1():
    w = int(input())
    sto = []
    for i in range(w):
        slo = input()
        sto.append(slo)
    print(*sto)

def zad2():
    st = []
    slova = str(input())
    st.append(slova)
    while slova != 'stop':
        slova = input()
        st.append(slova)
    print(*st[:-1])

def zad3():
    s = ''
    while s != 'stop':
        s = input()
        if 'ф' in s or 'Ф' in s:
            print('Ого! Это редкое слово!')
        else:
            print('Эх, это не очень редкое слово...')

def zad4():
    from random import randint
    che1 = 0
    che2= 0
    while che1 != 3:
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        ans = int(input(f'{num1} + {num2} = '))
        if ans != (num1 + num2):
            che1 += 1
            print('Ответ неверный')
        else:
            che2 += 1
            print('Правильно!')
    print('Игра окончена. Правильных ответов:', che2)


zad1()
zad2()
zad3()
zad4()