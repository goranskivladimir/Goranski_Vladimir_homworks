# Есть словарь песен группы Depeche Mode violator songsdict =
#     { 'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30,
# 'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68, }
#  Выведите общее время звучания всех песен. Создайте список песен,
#  \время звучаниях которых больше 5 минут Создайте новый словарь тех песен, в название которых состоит из одного слова
songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 5.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}
# Общее время звучания всех песен
total_duration = sum(songs_dict.values())
print(f"Общее время звучания всех песен: {total_duration} минут")

# Список песен, время звучания которых больше 5 минут
long_songs = [song for song, duration in songs_dict.items() if duration > 5]
print(f"Песни с временем звучания более 5 минут: {long_songs}")

# Новый словарь с песнями, в названии которых состоит только одно слово
single_word_songs = {song: duration for song, duration in songs_dict.items() if len(song.split()) == 1}
print(f"Песни с названием из одного слова: {single_word_songs}")