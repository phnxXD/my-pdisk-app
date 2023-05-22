import requests
from bs4 import BeautifulSoup
import pyperclip

# specify the URL of the page to scrape
url = 'http://desivdo.com/?s=chut&s=chut'

# send a GET request to the URL and get the page content
response = requests.get(url)
content = response.content

# create a BeautifulSoup object with the page content
soup = BeautifulSoup(content, 'html.parser')

# find the list of related videos
related_videos = soup.select_one('#ajax_content > ul.video_list:nth-child(2)')

if related_videos:
    # extract the links from all the related videos
    links = [video['href'] for video in related_videos.find_all('a')]

    if links:
        # use a set to store the unique links
        unique_links = set()

        # iterate through the extracted links and print only the unique ones
        for link in links:
            if link not in unique_links:
                print(link)
                unique_links.add(link)
        
        # copy the links to the clipboard
        pyperclip.copy('\n'.join(unique_links))
        print('The links have been copied to the clipboard.')
    else:
        print('No related video links found.')
else:
    print('Related videos section not found on the page.')
