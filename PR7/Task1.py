class Movie:
    def __init__(self, title, director, year) -> None:
        self.title = title
        self.director = director
        self.year = year
    
    def display_movie_info(self):
        return f"Название: {self.title}, Режиссер: {self.director}, Год выпуска: {self.year}"

m = Movie("Тестовый фильм", "Тестовый режиссер", 2023)
print(m.display_movie_info())