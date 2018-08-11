import fresh_tomatoes
import media

toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toys that come to life',
                        'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=4KPTXpQehio')
#print(toy_story.storyline)
avatar = media.Movie('Avatar',
                     'A marine on an alien planet',
                     'http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg',
                     'https://www.youtube.com/watch?v=d1_JBMrrYw8')
#print(avatar.storyline)
#avatar.show_trailer()
troy = media.Movie('Troy',
                   'A battle story',
                   'https://upload.wikimedia.org/wikipedia/en/thumb/b/b8/Troy2004Poster.jpg/220px-Troy2004Poster.jpg',
                   'https://www.youtube.com/watch?v=znTLzRJimeY')
#troy.show_trailer()
school_of_rock = media.Movie('School of Rock',
                             'rocking school',
                             'http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg',
                             'https://www.youtube.com/watch?v=3PsUJFEBC74')

ratatouille = media.Movie('Ratatouille',
                          'storyline',
                          'http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg',
                          'https://www.youtube.com/watch?v=c3sBBRxDAqk')

midnight_in_paris = media.Movie('Midnight in Paris',
                                'storyline',
                                'http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg',
                                'https://www.youtube.com/watch?v=atLg2wQQxvU')

hunger_games = media.Movie('Hunger Games',
                           'storuline',
                           'https://upload.wikimedia.org/wikipedia/en/thumb/3/39/The_Hunger_Games_cover.jpg/220px-The_Hunger_Games_cover.jpg',
                           'https://www.youtube.com/watch?v=PbA63a7H0bo')

movies = [toy_story, avatar, troy, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
