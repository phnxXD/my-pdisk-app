import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import concurrent.futures

def extract_video_link(webpage_url):
    # Send a GET request to the webpage
    response = requests.get(webpage_url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the button element with id "downloadbtn235"
    button_element = soup.find('button', id='downloadbtn235')

    if button_element:
        # Find the img element within the button element
        img_element = button_element.find('img', class_='vanb')

        if img_element:
            # Extract the video URL from the 'onclick' attribute
            onclick_attr = img_element.get('onclick')
            start_index = onclick_attr.find("'") + 1
            end_index = onclick_attr.rfind("'")
            video_url = onclick_attr[start_index:end_index]

            # Extract the desired part of the video link
            start_index = video_url.find('https://')
            end_index = video_url.find('.mp4') + len('.mp4')
            desired_video_link = video_url[start_index:end_index]
            return desired_video_link
    
    return None

# Read URLs from pdisk.txt
with open('pdisk.txt', 'r') as file:
    urls = file.readlines()

urls = [url.strip() for url in urls]

extracted_links = []
progress_bar = tqdm(total=len(urls), desc='Progress', unit='link')

# Extract video links concurrently
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for url in urls:
        future = executor.submit(extract_video_link, url)
        futures.append(future)

    for future in concurrent.futures.as_completed(futures):
        video_link = future.result()
        if video_link:
            extracted_links.append(video_link)
        progress_bar.update(1)

progress_bar.close()

# Save extracted video links to pdisko.txt
with open('pdisko.txt', 'w') as file:
    for link in extracted_links:
        file.write(link + '\n')
    
