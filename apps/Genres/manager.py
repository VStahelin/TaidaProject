from Genres.models import Genre


def insertGenre(genre):
    try:
        gen = Genre.objects.filter(mal_id=genre.mal_id) if Genre.objects.filter(mal_id=genre.mal_id).exists() else None
        if gen is None:
            gen = Genre(genre)
            gen.save()
            print(gen.__class__)
            return gen
        else:
            print(gen.__class__)
            return gen
    except Exception as e:
        print(e)
