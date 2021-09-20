from requests import api
from snipeit import Assets

assets = Assets()


def get_hardware(url, api_key, limit):
    r = assets.get(url, api_key, limit)
    return r


def search_hardware(url, api_key, limit, search):
    r = assets.search(url, api_key, limit, keyword=search)
    return r


def get_hardware_by_tag(url, api_key, assset_tag):
    r = assets.getDetailsByTag(url, api_key, assset_tag)
    return r
