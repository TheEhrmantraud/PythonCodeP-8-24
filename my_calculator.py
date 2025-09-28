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

# Важные штучки
def for_bool(x):    # -> тута проверяемс циферки на True/False
    x=input('что-то').strip().lower()
    x=x.strip
    if x in ('true', 't', '1', 'yes', 'y'): return True
    if x in ('false', 'f', '0', 'no', 'n'): return False

def for_numb(x):    # -> тута проверяемс циферки на int/float
    try:            # -> попытка вспомнить как работает try/except for testing input numbers 
        if '.' in x: return float(x)
        if '.' not in x: return int(x)
    except:
        try:
            return float(x)
        except:
            return x
# Конец важных штучек

def logic():
    print('a и b (True, False или число)')
    a=for_bool(input('a: '))
    b=for_bool(input('b: '))
    pop = input('Операция (and / or/ not)').strip()
    if pop == 'and': print(a and b)
    elif pop == 'or': print(a or b)
    elif pop == 'not': print(not a)
    else: print('Неверная операция')
        
def sravneniya():
    a_noеt = input('a (Число или строка)')
    b_noеt = input('b (Число или строка)')
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
        print('Нельзя сранвить')

def identity():
    try:    
        a=ast.literal_eval(input('a (литералка, напр. 10, "hi", [1,2]): '))
    except:
        a=input('Строчка a: ')
    try:    
        b=ast.literal_eval(input('b (литералка, напр. 10, "hi", [1,2]): '))
    except:
        b=input('Строчка b: ')
    pop=input('is или is not?').strip().lower()
    if pop=='is': print(a is b)
    elif pop=='is not': print(a is not b)
    else: print('Неверная операция')


    #Здесь самый сок будет, но потом
#def logic():
    #Здесь самый сок будет, но потом


def main():         # -> Корень кода (кальки), сюда все def'ки подтягиваются, которые написаны (должны быть) выше
    while True:
        print('Привет, введи исполнимую операцию: ')
        num = input().strip()
        if num == '1': arifmet()
        elif num == '2': logic()
        elif num == '3': sravneniya()
        elif num == '4': identity()
        #elif num == '5': 
        else: print('Говно число')

if __name__=="__main__":    # -> Запук из под корня, трогает сразу main
    main()

