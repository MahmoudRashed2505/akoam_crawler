# Create Class for Series includes ( Name, Seasons, Episodes, Rating, Genre, Network, Summary, and Poster )
class Series:
    def __init__(self, name, number_of_episodes=0, genre='Un-Categorized', summary="N/A", poster='imgs/placeholder' ,url='#',
     seasons=1, rating=0, episodes=[]):
        self.name = name
        self.seasons = seasons
        self.number_of_episodes = number_of_episodes
        self.rating = rating
        self.genre = genre
        self.summary = summary
        self.poster = poster
        self.url = url
        self.episodes = []


class Episode:
    def __init__(self,epiosde_number,link):
        self.episode_number = epiosde_number
        self.link = link
        self.direct_download_link = ''

    def set_download_link(self,link):
        self.direct_download_link = link