def check_voter(name):
    voted = {}
    if voted.get(name):
        print("out!")

    else:
        voted[name] = True
        print("you have voted!")

def url_cache(url):
    cache = {}
    if cache.get(url):
        return cache[url]
    else:
        return "Loading the page"