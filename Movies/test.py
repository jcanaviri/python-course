from domain.Movie import Movie
from service.MovieList import MovieList

while True:
    print('Options')
    print('1.- Add movie')
    print('2.- Show movies')
    print('3.- Delete moviezs')
    print('4.- Exit')

    option = int(input('> '))

    if option == 1:
        movie_name = input('Enter a movie name: ')        
        movie = Movie(movie_name)
        MovieList.add_movie(movie)
    elif option == 2:
        MovieList.show_movies()
    elif option == 3:
        MovieList.delete_movies()
    elif option == 4:
        break
