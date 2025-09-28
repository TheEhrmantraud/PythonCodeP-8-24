import ast

def arifmet():
    a=int(input('a: '))
    b=int(input('b: '))
    arif=input('Операция: ')
    if arif == '+': print(a+b) 
    elif arif == '-': print(a-b)
    elif arif == '*': print(a*b)
    elif arif == '/':
        if b!=0: print(a/b)
        else: print('Error arifmetic')
    elif arif == '//':
        if b!=0: print(a//b)
        else: print('Error arifmetic')
    elif arif == '%':
        if b!=0: print(a%b)
        else: print('Error arifmetic') 
    elif arif == '**': print(a**b)
    else: print('Неизвестная операция')

# Важные штучки
def for_bool(sos):    # -> тута проверяемс циферки на True/False
    sos.strip().lower()
    if sos in ('true', 't', '1', 'yes', 'y'): return True
    if sos in ('false', 'f', '0', 'no', 'n'): return False

def for_numb(sos):    # -> тута проверяемс циферки на int/float
    try:            # -> попытка вспомнить как работает try/except for testing input numbers 
        if '.' in sos: return float(sos)
        if '.' not in sos: return int(sos)
    except:
        try:
            return float(sos)
        except:
            return sos
# Конец важных штучек

def logic():
    print('a и b (True, False или число)')
    a=for_bool(input('a: '))
    b=for_bool(input('b: '))
    pop = input('Операция (and / or/ not): ').strip()
    if pop == 'and': print(a and b)
    elif pop == 'or': print(a or b)
    elif pop == 'not': print(not a)
    else: print('Неверная операция')
        
def sravneniya():
    a_noеt = input('a (Число или строка): ')
    b_noеt = input('b (Число или строка): ')
    a = for_numb(a_noеt)
    b = for_numb(b_noеt)
    pop = input('Операция (== != > < >= <=): ').strip()
    try:
        if pop == '==': print(a==b)
        elif pop == '!=': print(a!=b)
        elif pop == '>': print(a>b)
        elif pop == '<': print(a<b)
        elif pop == '>=': print(a>=b)
        elif pop == '<=': print(a<=b)
        else: print('Неизвестная операция')
    except Exception:
        print('Нельзя сравнить')

def identity():
    try:    
        a=ast.literal_eval(input('a (литералка, напр. 10, "hi", [1,2]): '))
    except:
        a=input('Вы ввели строчку? Повторите-ка её a: ')
    try:    
        b=ast.literal_eval(input('b (литералка, напр. 10, "hi", [1,2]): '))
    except:
        b=input('Вы ввели строчку? Повторите-ка её b: ')
    pop=input('is или is not?: ').strip().lower()
    if pop=='is': print(a is b)
    elif pop=='is not': print(a is not b)
    else: print('Неверная операция')

def notka():
    xren = input('Контейнер у нас: (1)-Строка || (2)-Список: ').strip()
    if xren=='1':
        sos=input('Строка: ')
        sas=input('Подстрока: ')
        pop=input('Оператор (in/not in): ').strip().lower()
        if pop=="in": print(sas in sos)
        elif pop=="not in": print(sas not in sos)
        else: print('Неизвестный оператор')
    elif xren=='2':
        listok=input('Элементы через запятую: ').strip(',')
        listochek_litl=input('Элементик: ').strip()
        pop=input('Оператор: ').strip().lower()
        if pop=="in": print(listok in [x.strip() for x in listok])
        elif pop=="not in": print(listok not in [x.strip() for x in listok])
        else: print('Неизвестный оператор')
    else: print('Неизвестный контейнер')


def main():         # -> Корень кода (кальки), сюда все def'ки подтягиваются, которые написаны (должны быть) выше
    while True:
        print('\n\n\nПривет. Введи исполнимую операцию:\n\n1) Арифметика 2) Логика 3) Сравнения\n4) is/is not 5) in/not in\n0) Выход\n\n')
        num = input().strip()
        if num == '1': arifmet()
        elif num == '2': logic()
        elif num == '3': sravneniya()
        elif num == '4': identity()
        elif num == '5': notka()
        elif num == '0': break
        else: print('Выбери 0-5')

if __name__=="__main__":    # -> Запук из под корня, трогает сразу main
    main()

