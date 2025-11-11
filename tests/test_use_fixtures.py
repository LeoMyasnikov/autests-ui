
# Как использовать декоратор pytest.mark.usefixtures для применения фикстур в автотестах.
# Он позволяет подключить одну или несколько фикстур к тестам или классам, даже если сами тесты их не указывают в параметрах.
import pytest


@pytest.fixture
def clear_books_database():
    print("[FIXTURE] Удаляем все данные из базы данных")


@pytest.fixture
def fill_books_database():
    print("[FIXTURE] Создаем новые данные в базе данных")


# используем фикстуру для передачи в функцию, без необходимости указания как аргумент
@pytest.mark.usefixtures('clear_books_database')
def test_read_all_books_in_library():
    ...

# порядок указания фикстур очень важен!
@pytest.mark.usefixtures(
    'clear_books_database',
    'fill_books_database'
)
class TestLibrary:
    def test_read_book_from_library(self):
        ...

    def test_delete_book_from_library(self):
        ...