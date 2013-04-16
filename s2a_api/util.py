# S2A API Client common functions


def append_slash(url):
    """ Function which return URL ended with the slash "/" """
    if url[-1] == "/":
        return url
    return url + "/"
        
