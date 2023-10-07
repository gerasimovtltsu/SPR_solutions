class Song:
    def __init__(self, title, artits, year) -> None:
        self.title = title
        self.artist = artits
        self.year = year
    
    def display_song_info(self):
        return f"Название: {self.title}, Исполнитель: {self.artist}, Год выпуска: {self.year}"

s = Song("Тестовая песня", "Тестовый исполнитель", 2023)
print(s.display_song_info())