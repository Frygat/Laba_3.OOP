class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

        @property
        def name(self) -> str:
            """Возвращает название книги"""
            return self._name

        @property
        def author(self) -> str:
            """Возвращает автора книги"""
            return self._author

        def __setattr__(self, name, value):
            """Переопределяем метод для запрета установки значений name и author"""
            if self.__initialized__ and name in ('_name', '_author'):
                raise AttributeError(f"Невозможно изменить атрибут '{name}'")
            super().__setattr__(name, value)

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages
        """Конструктор класса PaperBook.

                Args:
                    name: Название книги.
                    author: Автор книги.
                    pages: Количество страниц.
                """

        super().__init__(name, author)  #для вызова конструктора родительского класса
        self.pages = pages

    @property
    def pages(self) -> int:
        """Возвращает количество страниц книги."""
        return self._pages
    @pages.setter
    def pages(self, value: int) -> None:
        """Устанавливает количество страниц книги.

        Args:
            value: Количество страниц.

        Raises:
            TypeError: Если значение не является целым числом.
            ValueError: Если значение меньше 1.
        """
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом.")
        if value < 1:
            raise ValueError("Количество страниц не может быть меньше 1.")
        self._pages = value

    def __str__(self) -> str:
        """Возвращает строковое представление бумажной книги."""
        return f"{super().__str__()}. Страниц: {self.pages}"

    def __repr__(self) -> str:
        """Возвращает строковое представление для создания объекта."""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"



class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        self.name = name
        self.author = author
        self.duration = duration
        """Конструктор класса AudioBook.

               Args:name: Название книги.
            author: Автор книги.
            duration: Продолжительность аудиокниги.
        """
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        """Возвращает продолжительность аудиокниги."""
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        """Устанавливает продолжительность аудиокниги.

        Args:
            value: Продолжительность аудиокниги.

        Raises:
            TypeError: Если значение не является числом с плавающей запятой.
            ValueError: Если значение меньше или равно 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть больше 0.")
        self._duration = value

    def __str__(self) -> str:
         """Возвращает строковое представление аудиокниги."""
         return f"{super().__str__()}. Продолжительность: {self.duration}"

    def __repr__(self) -> str:
         """Возвращает строковое представление для создания объекта."""
         return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"

if __name__ == "__main__":
    book = Book(name="There is no change on the western front", author="Eric Remark")
    print(book)  # Check __str__
    print(repr(book))  # Check __repr__

    paper_book = PaperBook(name="semiconductor devices", author="Chirkin", pages=500)
    print(paper_book) # Check __str__
    print(repr(paper_book)) # Check __repr__
    try:
        paper_book.pages = -10
    except ValueError as e:
        print(f"Ошибка pages: {e}")

    try:
        paper_book.pages = "строка"
    except TypeError as e:
        print(f"Ошибка pages: {e}")


    audio_book = AudioBook(name="The Martian", author="Andy Weir", duration=12.5)
    print(audio_book) # Check __str__
    print(repr(audio_book)) # Check __repr__

    try:
        audio_book.duration = 0
    except ValueError as e:
        print(f"Ошибка duration: {e}")

    try:
        audio_book.duration = "строка"
    except TypeError as e:
         print(f"Ошибка duration: {e}")