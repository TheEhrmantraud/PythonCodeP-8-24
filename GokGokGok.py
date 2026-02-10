from abc import ABC, abstractmethod
import json
import os

BOOKS_FILE = "books.txt"
USERS_FILE = "users.txt"



class Person(ABC):
    def __init__(self, name):
        self._name = name  # инкапсуляция

    @abstractmethod
    def menu(self):
        pass



class Book:
    def __init__(self, title, author, status="доступна"):
        self.title = title
        self.author = author
        self.status = status

    def to_dict(self):
        return {"title": self.title, "author": self.author, "status": self.status}


class User:
    def __init__(self, name, books=None):
        self.name = name
        self.books = books or []

    def to_dict(self):
        return {"name": self.name, "books": self.books}


class Librarian(Person):
    def __init__(self, name, library):
        super().__init__(name)
        self.library = library

    def menu(self):
        while True:
            print("\n--- Меню библиотекаря ---")
            print("1. Добавить книгу")
            print("2. Удалить книгу")
            print("3. Зарегистрировать пользователя")
            print("4. Список пользователей")
            print("5. Список книг")
            print("0. Выход")

            choice = input("Выбор: ")

            if choice == "1":
                self.library.add_book()
            elif choice == "2":
                self.library.remove_book()
            elif choice == "3":
                self.library.register_user()
            elif choice == "4":
                self.library.show_users()
            elif choice == "5":
                self.library.show_books()
            elif choice == "0":
                break


class Reader(Person):
    def __init__(self, name, library):
        super().__init__(name)
        self.library = library

    def menu(self):
        while True:
            print("\n--- Меню пользователя ---")
            print("1. Просмотреть доступные книги")
            print("2. Взять книгу")
            print("3. Вернуть книгу")
            print("4. Мои книги")
            print("0. Выход")

            choice = input("Выбор: ")

            if choice == "1":
                self.library.show_available_books()
            elif choice == "2":
                self.library.take_book(self._name)
            elif choice == "3":
                self.library.return_book(self._name)
            elif choice == "4":
                self.library.show_user_books(self._name)
            elif choice == "0":
                break



class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.load_data()

    def load_data(self):
        if os.path.exists(BOOKS_FILE):
            with open(BOOKS_FILE, "r", encoding="utf-8") as f:
                self.books = [Book(**json.loads(line)) for line in f]

        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, "r", encoding="utf-8") as f:
                self.users = [User(**json.loads(line)) for line in f]

    def save_data(self):
        with open(BOOKS_FILE, "w", encoding="utf-8") as f:
            for book in self.books:
                f.write(json.dumps(book.to_dict(), ensure_ascii=False) + "\n")

        with open(USERS_FILE, "w", encoding="utf-8") as f:
            for user in self.users:
                f.write(json.dumps(user.to_dict(), ensure_ascii=False) + "\n")

    # ---------- Библиотекарь ----------
    def add_book(self):
        title = input("Название: ")
        author = input("Автор: ")
        self.books.append(Book(title, author))
        self.save_data()
        print("Книга добавлена")

    def remove_book(self):
        title = input("Название книги для удаления: ")
        self.books = [b for b in self.books if b.title != title]
        self.save_data()
        print("Книга удалена")

    def register_user(self):
        name = input("Имя пользователя: ")
        self.users.append(User(name))
        self.save_data()
        print("Пользователь зарегистрирован")

    def show_users(self):
        for u in self.users:
            print(u.name, u.books)

    def show_books(self):
        for b in self.books:
            print(b.title, b.author, "-", b.status)

    # ---------- Пользователь ----------
    def show_available_books(self):
        for b in self.books:
            if b.status == "доступна":
                print(b.title, b.author)

    def take_book(self, user_name):
        title = input("Введите название книги: ")

        for b in self.books:
            if b.title == title:
                if b.status == "выдана":
                    print("Книга уже выдана")
                    return
                b.status = "выдана"

                for u in self.users:
                    if u.name == user_name:
                        u.books.append(title)

                self.save_data()
                print("Книга выдана")
                return
        print("Книга не найдена")

    def return_book(self, user_name):
        title = input("Введите название книги: ")

        for b in self.books:
            if b.title == title:
                b.status = "доступна"

        for u in self.users:
            if u.name == user_name and title in u.books:
                u.books.remove(title)

        self.save_data()
        print("Книга возвращена")

    def show_user_books(self, user_name):
        for u in self.users:
            if u.name == user_name:
                print("Ваши книги:", u.books)


def main():
    library = Library()

    print("Выберите роль:")
    print("1. Библиотекарь")
    print("2. Пользователь")

    role = input("Выбор: ")

    name = input("Введите имя: ")

    if role == "1":
        librarian = Librarian(name, library)
        librarian.menu()
    elif role == "2":
        reader = Reader(name, library)
        reader.menu()


if __name__ == "__main__":
    main()