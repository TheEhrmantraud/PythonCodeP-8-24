from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine("sqlite:///C:/Users/12/Downloads/МПТфайлы/PROJECTbyMPT/my_projectPython/SQLAlchemy/library.db", echo=True)
print(engine)

Base = declarative_base()



class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birth_year = Column(Integer)
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    year = Column(Integer)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")




Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Чтобы не было дублей
session.query(Book).delete()
session.query(Author).delete()
session.commit()











author1 = Author(name="Лев Толстой", birth_year=1828)
author2 = Author(name="Фёдор Достоевский", birth_year=1821)
author3 = Author(name="Михаил Булгаков", birth_year=1891)
session.add_all([author1, author2, author3])
session.commit()

book1 = Book(title="Война и мир", year=1869, author=author1)
book2 = Book(title="Анна Каренина", year=1877, author=author1)
book3 = Book(title="Преступление и наказание", year=1866, author=author2)
book4 = Book(title="Идиот", year=1869, author=author2)
book5 = Book(title="Мастер и Маргарита", year=1967, author=author3)
session.add_all([book1, book2, book3, book4, book5])
session.commit()
















print("\n\n\n\n\n\n\nИмена всех авторов:")
for author in session.query(Author).all():
    print(author.name)

print("\n\n\n\n\n\n\nСмена имени")
author_to_update = session.query(Author).filter_by(name="Фёдор Достоевский").first()
if author_to_update:
    author_to_update.name = "Ф.М.Достоевский"
    session.commit()
    for author in session.query(Author).filter_by(name="Ф.М. Достоевский").all():
        print()
        print(author)
        
print("\n\n\n\n\n\n\nКнига на удаление")
book_to_delete = session.query(Book).filter_by(title="Идиот").first()
if book_to_delete:
    session.delete(book_to_delete)
    session.commit()
    print()
    for book in session.query(Book).all():
        print(book.author, book.title)

print("\n\n\n\n\n\n\nВсе книги от новых к старым:")
for book in session.query(Book).order_by(Book.year.desc()).all():
    print(book.title, book.year)
    
print("\n\n\n\n\n\n\nКниги после 1950 года:")
for book in session.query(Book).filter(Book.year > 1950).all():
    print(book.title, book.year)
    
print("\n\n\n\n\n\n\nАвтор по имени Лев Толстой:")
found_author = session.query(Author).filter_by(name="Лев Толстой").first()
if found_author:
    print(found_author.name, found_author.birth_year)





# Количество через func.count()
print("\n\n\n\n\n\n\nКоличество книг:")
books_count = session.query(func.count(Book.id)).scalar()
print()
print(books_count)


print("\n\n\n\n\n\n\nПервые 3 книги в алфавитном порядке:")
for book in session.query(Book).order_by(Book.title).limit(3).all():
    print(book.title)



session.close()