from imdb.imdb import IMDB

if __name__ == '__main__':
    for film in IMDB.getmovies("new"):
        print(film.__dict__)
