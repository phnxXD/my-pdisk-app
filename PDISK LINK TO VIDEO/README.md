
# Video Link Extractor

This Python script extracts video links from webpages and saves them to a file. It utilizes the `requests`, `BeautifulSoup`, `tqdm`, and `concurrent.futures` libraries for web scraping and concurrent processing.

## Prerequisites

- Python 3.x
- Required libraries:
  - requests
  - BeautifulSoup
  - tqdm

## Installation

1. Clone or download the code repository.
2. Install the required libraries by running the following command:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Prepare a text file named `pdisk.txt` containing a list of URLs, each on a separate line. These URLs should point to webpages where you want to extract video links from.
2. Run the script by executing the following command:
   ```
   python video_link_extractor.py
   ```
3. The script will process each URL concurrently and extract the video links.
4. A progress bar will be displayed, indicating the progress of link extraction.
5. The extracted video links will be saved to a file named `pdisko.txt`.

## Customization

- You can modify the code to adjust the HTML parsing logic or video link extraction process based on the structure of the target webpages.
- The code currently extracts video links by searching for a specific button element with id "downloadbtn235" and an img element within it. Modify the code in the `extract_video_link` function if the structure of your target webpages is different.
- The extracted video links are saved to `pdisko.txt` by default. You can change the output file name or path by modifying the code in the last section.

## Notes

- This script uses concurrent processing to speed up the extraction process by processing multiple URLs concurrently. The number of concurrent threads can be adjusted based on the system resources and the number of URLs to process.
- The `tqdm` library is used to display a progress bar during the link extraction process, providing visual feedback on the progress.

## Disclaimer

- Please ensure that you have the necessary rights or permissions to scrape the webpages and extract the video links.
- Be mindful of any legal or ethical considerations regarding web scraping and respect the terms of service of the websites you are scraping.

## License

This code is provided under the MIT License.
