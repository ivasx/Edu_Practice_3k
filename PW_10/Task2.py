from Task1 import *

class EBook(Book):
    def __init__(self, inventory_number, author, title, page_count, year_published, file_format, file_size_mb):
        super().__init__(inventory_number, author, title, page_count, year_published)
        self.file_format = file_format
        self.file_size_mb = file_size_mb