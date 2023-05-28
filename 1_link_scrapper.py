import requests
from bs4 import BeautifulSoup

# specify the URL of the page to scrape
url = 'http://desivdo.com/'

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
        
        # save the links to a file named "links.txt"
        with open("links.txt", "w") as file:
            file.write('\n'.join(unique_links))
        print('The links have been saved in "links.txt" file.')
    else:
        print('No related video links found.')
else:
    print('Related videos section not found on the page.')

# copy the link from terminal 
# go to link.txt and copy the links 
# after that go to 2nd py 
#  and simply run
# links will be stored to output.txt
# go to 3_pdisk_upload.py and run
# File URLs written to uploads.txt after running 

