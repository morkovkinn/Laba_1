import doctest
from typing import Union


class Note:
    def __init__(self, note_name: str, alteration: str):
        '''
        Создание и подготовка к работе объекта "Нота"

        :note_name: Название самой ноты (для обозначения нот используются буквы от A до G латинского алфавита)
        :alteration: Знак альтерации при ноте (Либо отсутствует, либо диез (#), либо бемоль(b))

        Примеры:

        >>> note1 = Note('A', 'b') #инициализация экземпляра класса (в данном случае ноты Ля бемоль (Ab))

        '''

        self.validate_note(note_name)
        self.note_name = note_name

        self.validate_alteration(alteration)
        self.alteration = alteration
    def validate_note(self, note):
        if not isinstance(note, str):
            raise TypeError('Note name should be a string')
        if not note in ['A','B','C','D','E','F','G']:
            raise ValueError(f'There is no such note as {note}')

    def validate_alteration(self, char):
        if not isinstance(char, str):
            raise TypeError('Alteration characher should be a string')
        if not char in ['#', 'b', '']:
            raise ValueError('Note can be either natural, sharp (#) or flat (b)')

    def fifth_up(self):
        '''
        Функция, которая возвращает ноту на квинту выше исходной

        :return: Нота на квинту выше исходной

        Примеры:
        >>> note1 = Note('A', 'b')
        >>> note1.fifth_up() #ожидаемый результат - нота Eb (Note('E', 'b'))
        '''
        ...


class Chord:
    def __init__(self, root_note: Note, chord_type: str):
        '''
        Создание и подготовка к работе объекта "Аккорд"

        :root_note: Тоника аккорда (тоникой может являться любая нота)
        :chord_type: Тип аккорда (мажорный, минорный, увеличенный, уменьшенный, большой мажорный септ, малый мажорный септ, минорный септ)

        (в качестве примера рассмотрены только 7 основных типов аккордов, хотя на самом деле их гораздо больше)

        Примеры:

        >>> chord1 = Chord(Note('A', 'b'), 'm') #инициализация экземпляра класса (аккорд Ля бемоль минор (Abm))
        '''

        self.validate_root_note(root_note)
        self.root_note = root_note

        self.validate_chord_type(chord_type)
        self.chord_type = chord_type

    def validate_root_note(self, root_note):
        if not isinstance(root_note, Note):
            raise TypeError('Root note of a chord should be a Note(class)')

    def validate_chord_type(self, chord_type):
        if not isinstance(chord_type, str):
            raise TypeError
        if not chord_type in ['M', 'm', 'aug', 'dim', 'maj7', '7', 'm7']:
            raise ValueError('Wrong chord type')

    def change_type(self, сhord_type: str):
        '''
        Функция, меняющая тип аккорда на указанный пользователем

        :return: оккорд с той же тоникой, что и исходный, но другого типа

        Примеры:
        >>> chord1 = Chord(Note('A', 'b'), 'm')
        >>> chord1.change_type('maj7') #ожидаемый результат - Chord(Note('A', 'b'), 'maj7')
        '''
        ...

    def change_root(self, root_note: Note):
        '''
        Функция, меняющая тонику аккорда на указанную пользователем

        :return: оккорд того же типа, что и исходный, но с другой тоникой

        Примеры:
        >>> chord2 = Chord(Note('A', 'b'), 'm')
        >>> chord2.change_root(Note('C', alteration='')) #ожидаемый результат - Chord(Note('C', ''), 'm')
        '''
        ...


class Album:
    def __init__(self, artist: str, name: str, length: Union[int, float], tracks: list):
        '''
        Создание и подготовка к работе объекта "Альбом"

        :artist: Имя исполнителя
        :name: Название альбома
        :length: Длительность альбома
        :tracks: Список треков

        Примеры:

        >>> album1 = Album(artist='Nine Inch Nails', name='The Downward Spiral', length=3902, tracks=['track1', 'track3', 'track4']) #инициализация экземпляра класса
        '''
        self.validate_name(artist)
        self.artist = artist

        self.validate_name(name)
        self.name = name

        self.validate_length(length)
        self.length = length

        self.validate_tracklist(tracks)
        self.tracks = tracks

    def validate_name(self, name):
        if not isinstance(name, str):
            raise TypeError('Artist or album name should be a string')

    def validate_length(self, length):
        if not isinstance(length, (int, float)):
            raise TypeError(f'Album length should be either integer or float, not {type(length)}')
        if length < 0:
            raise ValueError('Album length cannot be less than zero')

    def validate_tracklist(self, tracklist):
        if not isinstance(tracklist, list):
            raise TypeError('Tracklist should be a list')

    def addtrack(self, trackname: str, length: Union[int, float]):
        '''
        Функция, добавляющая трек в список треков и изменяющая общую длительность альбома

        :trackname: название трека
        :length: длина трека

        :return: измененный альбом с добавленным треком и увеличенной длительностью

        Пример:
        >>> album2 = Album(artist='Nine Inch Nails', name='The Downward Spiral', length=3902, tracks=['track1', 'track3'])
        >>> album2.addtrack('track10', 365)
        '''

if __name__ == "__main__":
    doctest.testmod()
    pass
