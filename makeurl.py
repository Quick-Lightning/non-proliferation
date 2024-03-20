import requests
def makeURL(id):
    response = requests.get(f"https://vidsrc.to/embed/movie/tt{id}")
    if response.status_code == 404:
        tvresponse = requests.get(f"https://vidsrc.to/embed/tv/tt{id}")
        if tvresponse.status_code == 200:
            return(f"https://vidsrc.to/embed/tv/tt{id}")
        else:
            return("nuclear")
    elif response.status_code == 200:
        return(f"https://vidsrc.to/embed/movie/tt{id}")
    else:
        return("nuclear")

print(makeURL("1147717"))