import os

class MovieList:
    file_path = 'movies.txt'

    @classmethod
    def add_movie(cls, new_movie):
        with open(cls.file_path, 'a', encoding='utf-8') as my_file:
            my_file.write(f'{new_movie.name}\n')

    @classmethod
    def show_movies(cls):
        with open(cls.file_path, 'r', encoding='utf-8') as my_file:
            print(my_file.read())

    @classmethod
    def delete_movies(cls):
        print('deleting...')
        os.remove(cls.file_path)
