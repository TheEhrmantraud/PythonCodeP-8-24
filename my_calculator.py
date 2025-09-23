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
    x=input('что-то')
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
    #Доделать, тк не знаю что тут происходит уже


    #Здесь самый сок будет, но потом
#def logic():
#def logic():
#def logic():
#def logic():
    #Здесь самый сок будет, но потом


def main():         # -> Корень кода (кальки), сюда все def'ки подтягиваются, которые написаны (должны быть) выше
    while True:
        print('Привет, введи исполнимую операцию: ')
        num = input()
        if num == '1': arifmet()
        elif num == '2': logic()
        #elif num == '3':
        #elif num == '4': 
        #elif num == '5':
        #elif num == '6':
        else: print('Говно число')

if __name__=="__main__":    # -> Запук из под корня, трогает сразу main
    main()

