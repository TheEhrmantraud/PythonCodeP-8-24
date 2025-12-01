import os
import random

stat_dir = 'game_stat1'
stat_file = os.path.join(stat_dir, 'static.txt')

os.makedirs(stat_dir, exist_ok=True)


def save_stat(result):
    with open(stat_file, 'a', encoding='utf-8') as f:
        f.write(result)

def create_board(n):
    return [[' 'for _ in range(n)] for _ in range(n)]

def view_board(board):
    l = len(board)
    print('\n  ' + ' '.join(str(i) for i in range(l)))
    for i in range(l):
        print(i, '| ' + ' | '.join(board[i]) + ' |')
    print()


def bot(board):
    n = len(board)
    while True:
        x = random.randint(0, n-1)
        y = random.randint(0, n-1)
        if board[x][y] == ' ':
            return x,y    
    

def win(board, symbol):
    l = len(board)
    for i in range(l):
        if all(board[i][j] == symbol for j in range(l)):
            return True
        if all(board[j][i] == symbol for j in range(l)):
            return True
    
    
        # Диагонали
    if all(board[i][i] == symbol for i in range(l)):
        return True
    if all(board[i][l - i - 1] == symbol for i in range(l)):
        return True


def draw(board):
    return all(kl != " " for row in board for kl in row)

def game(pvp=True):
    n = int(input('Введите размер поля: '))
    board = create_board(n)
    player = random.choice(['X', 'O'])
    print(f"первый ходит: {player}")
    
    while(True):
        view_board(board)
        print(f'ходит: {player}')
        
        if player == 'O' and not pvp:
            x, y = bot(board)
            print(f'Бот сходил на ({x}, {y})')
            
        else:
            try:
                x = int(input('Введите строку: '))
                y = int(input('Введите столбец: '))
            except ValueError:
                print('Введите числа')
                continue
            
            #Проверка на края
            if not(0<=x<n and 0<=y<n):
                print('Вы вышли за края поля')
                continue
            if board[x][y]!=" ":
                print('Клетка занята')
                continue
            #Проверка на края
            
            
        board[x][y] = player
        
        
        
        #Проверка на победу    
        if win(board, player):
            view_board(board)
            print(f"Игрок {player} победил")
            save_stat(f"Победа {player}")
            break
        
        
        if draw(board, player):
            view_board(board)
            print("Ничья")
            save_stat("Ничья")
            break
        #Проверка на победу
        
        
        
        player = "X" if player == "O" else "O"
            
    




def main():
    while(True):
        print ('\n Выберите рижим игры: \n1) Игра против бота. \n2) Игра против игрока \n3)Выход')
        choce = int(input())
        if choce==1:
            game(pvp=False)
        elif choce==2:
            game(pvp=True)
        elif choce==3:
            print('Пока')
            break
        else:
            break
        
if __name__ == "__main__":
    main()