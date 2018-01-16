from imdb.imdb import IMDB
import time

if __name__ == '__main__':
    for film in IMDB.getmovies("new", time.strftime("%Y-%m")):
        print(film.__dict__)
