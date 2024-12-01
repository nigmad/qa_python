from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


import pytest

from main import BooksCollector  

def test_add_new_book_adds_book_with_empty_genre():
    collector = BooksCollector()
    collector.add_new_book("Книга 1")
    assert collector.get_books_genre() == {"Книга 1": ""}

def test_add_new_book_does_not_add_duplicate_books():
    collector = BooksCollector()
    collector.add_new_book("Книга 1")
    collector.add_new_book("Книга 1")
    assert len(collector.get_books_genre()) == 1

@pytest.mark.parametrize("book_name", ["", "A" * 41])
def test_add_new_book_invalid_name_does_not_add_book(book_name):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    assert len(collector.get_books_genre()) == 0

def test_set_book_genre_valid_genre_updates_books_genre():
    collector = BooksCollector()
    collector.add_new_book("Книга 1")
    collector.set_book_genre("Книга 1", "Фантастика")
    assert collector.get_book_genre("Книга 1") == "Фантастика"

def test_set_book_genre_invalid_genre_keeps_genre_empty():
    collector = BooksCollector()
    collector.add_new_book("Книга 1")
    collector.set_book_genre("Книга 1", "Неизвестный жанр")
    assert collector.get_book_genre("Книга 1") == ""

def test_get_book_genre_existing_book_returns_genre():
    collector = BooksCollector() 
    collector.add_new_book("Книга 1") 
    collector.set_book_genre("Книга 1", "Фантастика") 
    assert collector.get_book_genre("Книга 1") == "Фантастика" 

def test_get_book_genre_nonexistent_book_returns_none(): 
    collector = BooksCollector() 
    assert collector.get_book_genre("Несуществующая книга") is None

def test_get_books_with_specific_genre_returns_correct_books(): 
    collector = BooksCollector()
    collector.add_new_book("Книга 1") 
    collector.add_new_book("Книга 2") 
    collector.set_book_genre("Книга 1", "Фантастика") 
    collector.set_book_genre("Книга 2", "Ужасы") 
    assert collector.get_books_with_specific_genre("Фантастика") == ["Книга 1"] 

def test_get_books_genre_no_books_added_returns_empty_dict(): 
    collector = BooksCollector() 
    assert collector.get_books_genre() == {} 

def test_get_books_genre_books_added_returns_correct_dict(): 
    collector = BooksCollector() 
    collector.add_new_book("Книга 1") 
    collector.set_book_genre("Книга 1", "Фантастика") 
    assert collector.get_books_genre() == {"Книга 1": "Фантастика"}

def test_get_books_for_children_excludes_books_with_age_restricted_genres():
    collector = BooksCollector()
    collector.add_new_book("Книга 1")
    collector.add_new_book("Книга 2")
    collector.set_book_genre("Книга 1", "Фантастика") # Фантастика не имеет возрастного ограничения 
    collector.set_book_genre("Книга 2", "Ужасы") # Ужасы имеют возрастное ограничение
    assert collector.get_books_for_children() == ["Книга 1"]

def test_add_book_in_favorites_existing_book_adds_to_favorites():
    collector = BooksCollector()
    collector.add_new_book("Книга 1")
    collector.add_book_in_favorites("Книга 1")
    assert collector.get_list_of_favorites_books() == ["Книга 1"]

def test_add_book_in_favorites_does_not_add_nonexistent_book():
    collector = BooksCollector()
    collector.add_book_in_favorites("Книга 1")
    assert collector.get_list_of_favorites_books() == []

def test_delete_book_from_favorites_existing_book_removes_from_favorites():
    collector = BooksCollector()
    collector.add_new_book("Книга 1")
    collector.add_book_in_favorites("Книга 1")
    collector.delete_book_from_favorites("Книга 1")
    assert collector.get_list_of_favorites_books() == []

def test_get_list_of_favorites_books_returns_correct_list():
    collector = BooksCollector()
    collector.add_new_book("Книга 1")
    collector.add_new_book("Книга 2")
    collector.add_book_in_favorites("Книга 1")
    assert collector.get_list_of_favorites_books() == ["Книга 1"]

def test_get_list_of_favorites_books_multiple_books_returns_only_favorites(): 
    collector = BooksCollector() 
    collector.add_new_book("Книга 1") 
    collector.add_new_book("Книга 2") 
    collector.add_book_in_favorites("Книга 1")
    assert collector.get_list_of_favorites_books() == ["Книга 1"]


