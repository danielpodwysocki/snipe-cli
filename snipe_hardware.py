from snipeit import Assets

A = Assets()


def get_hardware(url, api_key, limit):
    r = A.get(url, api_key, limit)
    return r
