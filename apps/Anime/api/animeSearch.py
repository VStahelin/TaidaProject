from jikanpy import Jikan

from Anime.models import AnimeCard


def animeSearch(search_field):
    jikan = Jikan()
    response = jikan.search('anime', search_field)
    return response.get('results')
