import sqlite3

class Book:
    def __init__(self, inventory_number, author, title, page_count, year_published):
        self.inventory_number = inventory_number
        self.author = author
        self.title = title
        self.page_count = page_count
        self.year_published = year_published

    def __str__(self):
        return (f"{self.inventory_number} | "
                f"{self.author} | "
                f"{self.title} | "
                f"{self.page_count} стор. | "
                f"{self.year_published} р.")

    @staticmethod
    def add_book(book):
        try:
            cursor.execute('''
                           INSERT INTO books (inventory_number, author, title, page_count, year_published)
                           VALUES (?, ?, ?, ?, ?)
                           ''', (book.inventory_number, book.author, book.title, book.page_count, book.year_published))
            conn.commit()
            print(f'Книга {book.title} успішно додана до бази даних.')
        except sqlite3.IntegrityError:
            print('Книгу не додано. Книга з таким інвентарним номером уже існує в базі даних.')
        except Exception as error:
            print(f'Книгу не додано. Помилка: {error}')

    @staticmethod
    def search_book_by_author(author):
        try:
            cursor.execute('SELECT * FROM books WHERE LOWER(author) = LOWER(?)', (author,))
            result = cursor.fetchall()
            if not result:
                print('Книг за таким автором не знайдено.')
                return []
            return [Book(*row) for row in result]
        except Exception as error:
            print(f'Книгу за таким автором не знайдено. Помилка: {error}')
            return []
    @staticmethod
    def sort_books_by_year(reverse=False):
        try:
            if reverse:
                cursor.execute('SELECT * FROM books ORDER BY year_published DESC')
            else:
                cursor.execute('SELECT * FROM books ORDER BY year_published')
            result = cursor.fetchall()
            return [Book(*row) for row in result]
        except Exception as error:
            print(f'Щось пішло не так. Помилка: {error}')
            return []



conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        inventory_number TEXT PRIMARY KEY,
        author TEXT,
        title TEXT,
        page_count INTEGER,
        year_published INTEGER
        )
    ''')

conn.commit()


if __name__ == '__main__':
    print("=== ДОДАВАННЯ ЗВИЧАЙНИХ КНИГ ===")
    Book.add_book(Book('NL1.11111111', 'Лі Бардуґо', 'Шістка воронів', 480, 2015))
    Book.add_book(Book('NL1.12112112', 'Агата Крісті', 'Вбивство у "Східному експресі"', 256, 1934))
    Book.add_book(Book('NL1.11312111', 'Дженіфер Арментраут', 'Із крові й попелу', 636, 2020))
    Book.add_book(Book('NL1.11111121', 'Орест Субтельний', 'Історія України', 720, 1991))
    Book.add_book(Book('NL1.11984111', 'Джордж Орвелл', '1984', 328, 1949))
    Book.add_book(Book('NL1.12112118', 'Агата Крісті', 'Вбивство за абеткою', 320, 1936))
    Book.add_book(Book('NL1.12112119', 'Агата Крісті', 'Німий свідок', 304, 1937))
    Book.add_book(Book('NL1.11141351', 'Лілет Ноні', 'Тюремна цілителька', 416, 2022))

    print('\nПОШУК: книги Агати Крісті')
    for book in Book.search_book_by_author('Агата Крісті'):
        print(book)

    print('\nСОРТУВАННЯ: книги за роком видання (від нових до старих)')
    for book in Book.sort_books_by_year(True):
        print(book)

    conn.close()