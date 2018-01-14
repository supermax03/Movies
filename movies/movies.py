class Movie:
    def __init__(self, title, director, duration, genre, summary, cast, trailers):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.summary = summary
        self.director = director
        self.cast = cast
        self.trailers = trailers

    def addActor(self, *actors):
        for actor in actors:
            self.cast.append(actor)

    def addTrailer(self, *trailers):
        for trailer in trailers:
            self.trailers.append(trailer)

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def setDuration(self, duration):
        self.duration = duration

    def getDuration(self):
        return self.duration

    def getSummary(self):
        return self.summary

    def setSummary(self, summary):
        self.summary = summary

    def setDirector(self, director):
        self.director = director

    def getDirector(self):
        return self.director

    def getGenre(self):
        return self.genre

    def setGenre(self, genre):
        self.genre = genre

    def getTrailers(self):
        return self.trailers

    def getCast(self):
        return self.cast

    Title = property(fget=getTitle, fset=setTitle)
    Duration = property(fget=getDuration, fset=setDuration)
    Summary = property(fget=setSummary, fset=setSummary)
    Genre = property(fget=getGenre, fset=setGenre)
    Director = property(fget=getDirector, fset=setDirector)
    Trailers = property(fget=getTrailers)
    Cast = property(fget=getCast)
