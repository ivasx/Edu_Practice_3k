from Task1 import *

class EBook(Book):
    def __init__(self, inventory_number, author, title, page_count, year_published, file_format, file_size_mb):
        super().__init__(inventory_number, author, title, page_count, year_published)
        self.file_format = file_format
        self.file_size_mb = file_size_mb

    def __str__(self):
        base_str = super().__str__()
        return (f'{base_str} | '
                f'Формат: {self.file_format} | '
                f'Розмір: {self.file_size_mb} MB')

    @staticmethod
    def add_ebook(ebook):
        try:
            cursor.execute('''
                           INSERT INTO ebooks (inventory_number, author, title, page_count, year_published, file_format, file_size_mb)
                           VALUES (?, ?, ?, ?, ?, ?, ?)
                           ''', (ebook.inventory_number, ebook.author, ebook.title, ebook.page_count, ebook.year_published, ebook.file_format, ebook.file_size_mb))
            conn.commit()
            print(f'Електронна книга {ebook.title} успішно додана до бази даних.')
        except sqlite3.IntegrityError:
            print('Електронну книгу не додано. Книга з таким інвентарним номером уже існує в базі даних.')
        except Exception as error:
            print(f'Електронну книгу не додано. Помилка: {error}')

    @staticmethod
    def search_ebook_by_author(author):
        try:
            cursor.execute('SELECT * FROM ebooks WHERE LOWER(author) = LOWER(?)', (author,))
            result = cursor.fetchall()
            if not result:
                print('Електронних книг за таким автором не знайдено.')
                return []
            return [EBook(*row) for row in result]
        except Exception as error:
            print(f'Помилка пошуку: {error}')
            return []

    @staticmethod
    def search_ebook_by_format(file_format):
        try:
            cursor.execute('SELECT * FROM ebooks WHERE LOWER(file_format) = LOWER(?)', (file_format,))
            result = cursor.fetchall()
            if not result:
                print(f'Електронних книг у форматі {file_format} не знайдено.')
                return []
            return [EBook(*row) for row in result]
        except Exception as error:
            print(f'Помилка пошуку: {error}')
            return []

    @staticmethod
    def sort_ebooks_by_size(reverse=False):
        try:
            if reverse:
                cursor.execute('SELECT * FROM ebooks ORDER BY file_size_mb DESC')
            else:
                cursor.execute('SELECT * FROM ebooks ORDER BY file_size_mb')
            result = cursor.fetchall()
            return [EBook(*row) for row in result]
        except Exception as error:
            print(f'Помилка сортування: {error}')
            return []

    def get_reading_time(self, reading_speed_pages_per_hour=50):
        hours = self.page_count / reading_speed_pages_per_hour
        return f"Приблизний час читання: {hours:.1f} годин"

    def is_large_file(self, threshold_mb=100):
        return self.file_size_mb > threshold_mb


cursor.execute('''
    CREATE TABLE IF NOT EXISTS ebooks (
        inventory_number TEXT PRIMARY KEY,
        author TEXT,
        title TEXT,
        page_count INTEGER,
        year_published INTEGER,
        file_format TEXT,
        file_size_mb REAL
    )
''')
conn.commit()

#Потрібно дописати тест
if __name__ == '__main__':
    print("=== ДОДАВАННЯ ЕЛЕКТРОННИХ КНИГ ===")

    # Створення та додавання електронних книг
    EBook.add_ebook(EBook('EB1.11111111', 'Стівен Кінг', 'Воно', 1138, 1986, 'PDF', 25.6))
    EBook.add_ebook(
        EBook('EB1.22222222', 'Дж.К. Роулінг', 'Гаррі Поттер і філософський камінь', 223, 1997, 'EPUB', 12.3))
    EBook.add_ebook(EBook('EB1.33333333', 'Орсон Скотт Кард', 'Гра Ендера', 324, 1985, 'MOBI', 18.7))
    EBook.add_ebook(EBook('EB1.44444444', 'Френк Герберт', 'Дюна', 688, 1965, 'PDF', 156.8))
    EBook.add_ebook(EBook('EB1.55555555', 'Стівен Кінг', 'Сяйво', 447, 1977, 'EPUB', 22.1))
    EBook.add_ebook(EBook('EB1.66666666', 'Джордж Р.Р. Мартін', 'Гра престолів', 694, 1996, 'PDF', 89.4))

    print('\n=== ПОШУК ЕЛЕКТРОННИХ КНИГ ЗА АВТОРОМ ===')
    print('ПОШУК: електронні книги Стівена Кінга')
    for ebook in EBook.search_ebook_by_author('Стівен Кінг'):
        print(ebook)

    print('\n=== ПОШУК ЕЛЕКТРОННИХ КНИГ ЗА ФОРМАТОМ ===')
    print('ПОШУК: електронні книги у форматі PDF')
    for ebook in EBook.search_ebook_by_format('PDF'):
        print(ebook)

    print('\n=== СОРТУВАННЯ ЕЛЕКТРОННИХ КНИГ ЗА РОЗМІРОМ ===')
    print('СОРТУВАННЯ: електронні книги за розміром файлу (від найбільших до найменших)')
    for ebook in EBook.sort_ebooks_by_size(reverse=True):
        print(ebook)

    print('\n=== ДОДАТКОВІ ФУНКЦІЇ ЕЛЕКТРОННИХ КНИГ ===')
    test_ebook = EBook('EB1.77777777', 'Тестовий автор', 'Тестова книга', 400, 2023, 'EPUB', 75.5)

    print(f'Назва книги: {test_ebook.title}')
    print(f'Кількість сторінок: {test_ebook.page_count}')
    print(f'Розмір файлу: {test_ebook.file_size_mb} MB')
    print(test_ebook.get_reading_time())  # З швидкістю 50 сторінок/годину
    print(test_ebook.get_reading_time(30))  # З швидкістю 30 сторінок/годину
    print(f'Чи є файл великим (>100 MB)? {test_ebook.is_large_file()}')

    large_ebook = EBook('EB1.88888888', 'Великий автор', 'Велика книга', 1500, 2020, 'PDF', 150.0)
    print(f'Чи є файл "{large_ebook.title}" великим (>100 MB)? {large_ebook.is_large_file()}')

    print('\n=== ДЕМОНСТРАЦІЯ НАСЛІДУВАННЯ ===')
    print('Електронна книга як об\'єкт класу Book:')
    print(f'Автор: {test_ebook.author}')
    print(f'Назва: {test_ebook.title}')
    print(f'Рік видання: {test_ebook.year_published}')
    print('Електронна книга з додатковими полями:')
    print(f'Формат файлу: {test_ebook.file_format}')
    print(f'Розмір файлу: {test_ebook.file_size_mb} MB')

    conn.close()