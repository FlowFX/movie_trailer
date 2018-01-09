# Provide magic code that generates the HTML.
import fresh_tomatoes
# Provide essential class media.Movie.
import media


toy_story = media.Movie(
    'Toy Story',
    'A story of a boy and its toys that come alive.',
    'http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg',
    'https://www.youtube.com/watch?v=KYz2wyBy3kc',
)

avatar = media.Movie(
    'Avatar',
    'A marine on an alien planet.',
    'http://www.impawards.com/2009/posters/avatar_xlg.jpg',
    'https://www.youtube.com/watch?v=5PSNL1qE6VY',
)

blues_brothers = media.Movie(
    'Blues Brothers',
    'Two brothers bring the band back together.',
    'http://www.impawards.com/1980/posters/blues_brothers_ver1_xlg.jpg',
    'https://www.youtube.com/watch?v=A-xtJYIwfYo',
)

the_commitments = media.Movie(
    'The Commitments',
    'An Irish soul band plays a concert without Wilson Picket.',
    'http://www.impawards.com/1991/posters/commitments.jpg',
    'https://www.youtube.com/watch?v=3paf2TLrgsg',
)

sneakers = media.Movie(
    'Sneakers',
    'An epic battle of two computer hackers.',
    'http://www.impawards.com/1992/posters/sneakers.jpg',
    'https://www.youtube.com/watch?v=8X_yiqK_sUs',
)

first_blood = media.Movie(
    'First Blood',
    'A forest hike goes bad.',
    'http://www.impawards.com/1982/posters/first_blood_ver1.jpg',
    'https://www.youtube.com/watch?v=IAqLKlxY3Eo',
)

movies = [
    toy_story,
    avatar,
    blues_brothers,
    the_commitments,
    sneakers,
    first_blood,
    ]

# Generate an HTML page and open it in the browser
fresh_tomatoes.open_movies_page(movies)
