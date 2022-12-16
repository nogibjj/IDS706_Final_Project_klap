from movie_reviews import generate


def test():
    df_sample = generate.generate_reviews("imdb", 10)
    assert df_sample.shape[0] == 10
    return