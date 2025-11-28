import os
import random

stat_dir = 'game_stat'
stat_file = os.path.join(stat_dir, 'static.txt')

os.mkdir(stat_dir, exit=True)


def save_stat(result):
    with open(stat_file, 'a', encoding='utf-8') as f:
        f.write(result)

def create_board(n):
    return [[' 'for _ in range(n)] for _ in range(n)]

def view_board(board):
    l = len(board)
    print()


def draw():
    pass
def win():
    pass

def game():
    n = int(input('Введите размер поля: '))
    board = create_board(n)





def main():
    while(True):
        print ('\n Выберите рижим игры: \n1) Игра против бота. \n2) Игра против игрока \n3)Выход')
        choce = int(input())
        if choce==1:
            game()
        if choce==2:
            game()
        if choce==3:
            print('Пока')
            break
        
if __name__ == "__main__":
    main()
    