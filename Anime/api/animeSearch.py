from jikanpy import Jikan

from Anime.models import AnimeCard


def animeSearch(search_field):
    jikan = Jikan()
    response = jikan.search('anime', search_field)
    animeList = []
    for animeDict in response.get('results'):
        anime = AnimeCard()
        anime.title = animeDict.get('title')
        anime.mal_id = animeDict.get('mal_id')
        anime.synopsis = animeDict.get('synopsis')
        anime.image_url = animeDict.get('image_url')
        animeList.append(anime)

    return animeList
