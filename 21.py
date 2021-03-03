import random
import sys

s = ['2', '5', '4333', '7', '5', '3', '45']
s1 = [2, 5, 4333, 7, 5, 3, 45]
#1
print('#1: ',[int(i) for i in s])
#2
print('#2: ',len(set(s)))
#3
print('#3: ',s[::-1])
#4
print('#4: ',[i for i in range(len(s)) if s[i]=='5'])
#5
print('#5: ',sum(int(i) for i in s[1::2]))
#6
print ('#6: ', max(s,key=len))

#7 сократите код...
i = 0
['much','code','wow'][i]

#8 генерирует (не просто выдает готовый) список всех названий групп
def generate_groups():
    name = 'BKMH'
    g1=[]
    k = name[0]
    for k in name:
        for i in range(1,10):
            if (k == name[0]):
               g1.append(k+str(i))
               if (i==1):
                    for j in range(4): g1.append(k+str(i)+str(j))
            if (k==name[1]):
                g1.append(k+str(i))
                if (i==1):
                    for j in range(10): g1.append(k+str(i)+str(j))
                elif (i==2):
                    for j in range(6): g1.append(k+str(i)+str(j))
            if (k==name[2]):
                g1.append(k+str(1))
                g1.append(k+str(2))
                break
            else:
                g1.append(k+str(i))
                if (i==1):
                    g1.append(k+str(i)+'0')
                
    return g1
print('#8: ',generate_groups())

# 9 zip()
def transpose(array):
    f=0
    array_transpose =[[0,0,0],[0,0,0],[0,0,0]]
    for i, j, k in zip(array[0], array[1], array[2]):
        array_transpose[f][0] = i
        array_transpose[f][1] = j
        array_transpose[f][2] = k
        f+=1
    return array_transpose
print('#9: ',transpose([[1,2,3],[4,5,6],[7,8,9]]))

# 10 генератор доклада
def generate_doc():
    words = [['Коллеги,', 'В то же время,', 'Однако,', 'Тем не менее,', 'Следовательно,',
         'Соответственно,', 'Вместе с тем,','С другой стороны,'],
        ['парадигма цифровой экономики', 'контекст цифровой трансформации','диджитализация бизнес-процессов',
         'прагматичный подход к цифровым платформам', 'совокупность сквозных технологий',
         'программа прорывных исследований', 'ускорение блокчейн-транзакций', 'экспоненциальный рост Big Data'],
    ['открывает новые возможности для','выдвигает новые требования','несёт в себе риски',
     'расширяет горизонты', 'заставляет искать варианты', 'не оставляет шанса для','повышает вероятность', 'обостряет проблему'],
    ['дальнейшего углубления', 'бюджетного финансирования', 'синергетического эффекта', 'компрометации конфиденциальных',
     'универсальной коммодитизации', 'несанкционированной кастомизации', 'нормативного регулирования','практического применения'],
    ['знаний и компетенций.', 'непроверенных гипотез.', 'волатильных активов.', 'опасных экспериментов.', 'государственно-частных партнёрств.',
     'цифровых следов граждан.', '	нежелательных последствий.', '	внезапных открытий.']]
    report = ''
    for i in range(random.randint(1,5)):
        for j in range (random.randint(0,5)):
            for k in range(5):
                report += words[k][random.randint(0,7)]+' '
        report +='\n'
    return report

print ('#10: ',generate_doc())

#11 внизу

#12 функция, которая принимает только именованные аргументы
def get_multiple(*keys, name):
    return 'hello '+name

print('#12: ',get_multiple(name = 'Evgenia'))



#13 генератор имен
def generate_name():
    names = ['Данил', 'Роман', 'Лев', 'Ильдар', 'Николай', 'Данила',
              'Табян', 'Семен', 'Самир', 'Тамерлан', 'Святослав',
              'Герман', 'Тамерлан', 'Назар','Степан', 'Леонид']
    second_name3 = ['ий', 'як', 'ич', 'ев', 'нц', 'ян', 'ко', 'ин', 'ов', 'ский', 'цкий', 'их']
    a = "АЕИОУЭЮЯЁ"
    b = 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
    c= "АЕИОУЭЮЯЁБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
    allNames=''
    for i in range(6):
        second_name = c[random.randint(0,29)]
        for i in range(random.randint(2,3)):
            second_name +=a[random.randint(0,8)].lower() + b[random.randint(0,20)].lower()
        allNames += names[random.randint(0,15)]+' '+ c[random.randint(0,29)] + '. '+ second_name + second_name3[random.randint(0,11)] +'\n'
    return allNames
print ('#13: ',generate_name())

#14
#is проверяет, что переменные указывают на один и тот же объект в памяти.
# Но особенность в том, что, для экономии памяти, булевы типы, числа и строки могут кешироваться.
# is проверяет, что переменные указывают на один и тот же объект в памяти.
# Но особенность в том, что, для экономии памяти, булевы типы, числа и строки могут кешироваться.
# если сделать строку длиннее то вывод станет правильным

# 15 создание многомерного массива с помощью вложенных списков.
def generate_array(d1,d2=0,d3=0,d4=0, d5=0, d6=0, d7=0):
    array=[]
    dim = [d2, d3, d4, d5, d6, d7]
    for j in range(d1):
        array.append([])
    for i in range(d1):
        for j in range (dim[i]):
            array[i].append(['he'])
    return array

print('#15: ',generate_array(3,3,4,2))

#11 Реализуйте свою версию print()
def print(a):
    str_1 = ''
    if (isinstance(a, list)):
        str_1+='['
        for i in range (len(a)-1): str_1+= str(a[i]) + ', '
        str_1+= a[-1]+']'
    else: str_1=str(a)
    sys.stdout.write(str_1+'\n')

print (['h',5,'ghgdf'])
