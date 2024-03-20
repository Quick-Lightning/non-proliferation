from imdb import Cinemagoer
from makeurl import makeURL
titles = []
daBase =  Cinemagoer()

def search(query, n):
    try:
        dresults = {}
        for x in range (0, n):
            if makeURL(daBase.search_movie(query)[x].getID()) != "nuclear":
                dresults[daBase.search_movie(query)[x]["title"]] = daBase.search_movie(query)[x].getID()
            else:
             n = n + 1
        return(dresults)
    except Exception as e:
        return("error")

