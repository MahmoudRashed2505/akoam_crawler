from urllib import response
from bs4 import BeautifulSoup
import requests
from os import system
from tqdm import tqdm
from series import Series,Episode


def get_series_list():

    response = requests.get("https://akwam.im/series?section=0&category=87&rating=0&year=2022&language=0&formats=0&quality=0&page=1")
    soup = BeautifulSoup(response.text, 'html.parser')
    system("cls")
    ramdan_series = []
    print("Getting Ramdan Series List For Each Page")
    for i in range(0,len(soup.find_all('li', class_='page-item mx-1'))):

        response = requests.get("https://akwam.im/series?section=0&category=87&rating=0&year=2022&language=0&formats=0&quality=0&page="+str(i+1))
        series = soup.find_all("div",class_="entry-image")
        print("\nGetting data for page number "+str(i+1))
        for serie in tqdm(series):
            new_series = Series(name=serie.find("img")['alt'],url=serie.find("a")["href"],poster=serie.find("img")["src"])
            print(new_series.poster)
            get_series_details(new_series)
            get_series_episodes(new_series)
            ramdan_series.append(new_series)

    print("Done Scrapping Series")
    return ramdan_series


def get_series_details(series):
   
    response = requests.get(series.url)
    soup = BeautifulSoup(response.text, 'html.parser')
    series.summary = soup.find_all("h2")[2].text
    series.number_of_episodes = len(soup.find("div",class_="bg-primary2 p-4 col-lg-4 col-md-6 col-12"))
    

def get_series_episodes(series):
   
    series_episodes = []
    response = requests.get(series.url)
    soup = BeautifulSoup(response.text, 'html.parser')
    episodes = soup.find_all("div",class_="bg-primary2 p-4 col-lg-4 col-md-6 col-12")
    for index,episode in enumerate(episodes):
        new_episode = Episode(index+1,episode.find("a")["href"])
        get_direct_download_link(new_episode)
        series_episodes.append(new_episode)
     
    series.episodes = series_episodes
   
    
def get_direct_download_link(episode):
    response = requests.get(episode.link)
    soup = BeautifulSoup(response.text, 'html.parser')
    episode_download_link = soup.find("a",class_="link-btn link-download d-flex align-items-center px-3")["href"]
    response = requests.get(episode_download_link)
    soup = BeautifulSoup(response.text, 'html.parser')
    episode_download_page = [href['href'] for href in soup.find_all("a")]
    episode_download_page = episode_download_page[3]
    response = requests.get(episode_download_page)
    soup = BeautifulSoup(response.text, 'html.parser')
    episode_download_link = soup.find("a",class_="link btn btn-light")["href"]
   
    episode.set_download_link(episode_download_link)
   
