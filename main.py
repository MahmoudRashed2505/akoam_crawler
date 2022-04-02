from get_series_list import get_series_list
import os
import requests
from tqdm import tqdm

def main():
    
    Ramdan_Series = get_series_list()

    # Check if folder Series is exists
    if not os.path.exists('Series'):
        os.makedirs('Series')
    else:
        os.chdir('Series')
    print("Downloading Ramdan Series")
    # For each series in Ramdan Series we create a folder with the name of the series
    for series in tqdm(Ramdan_Series):
        s_name = ''.join(letter for letter in series.name if letter.isalnum())
        if not os.path.exists(s_name):
            os.makedirs(s_name)
        # Change directory to the series folder
        os.chdir(s_name)
        # Save the poster of the series in the folder and txt file containing the summary of the series
        # Save text file containing series episodes direct download links
        with open('poster.png','wb') as f:
            f.write(requests.get(series.poster).content)
        with open('summary.txt','w',encoding='utf-8') as f:
            f.write(series.summary)
        with open('episodes.txt','w') as f:
            for episode in series.episodes:
                f.write(episode.direct_download_link+'\n')
        # Change directory to the parent folder
        os.chdir('..')
    print("Done")

if __name__ == '__main__':
    main()