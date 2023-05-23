import threading
import requests
from urllib.parse import urlparse

def first_code():
    # Read links from file
    with open('links.txt', 'r') as file:
        links = file.read().splitlines()

    # Process links
    output = []
    for link in links:
        result_with_emojis = remove_domain_format_capitalize_and_add_emoji(link)
        output.append(result_with_emojis)

    # Save output to file
    with open('output.txt', 'w') as file:
        file.write('\n'.join(output))

    print("Running first code...")
    # Simulating some work
    for i in range(5):
        print("First code: Working...")
    
    print("First code finished!")

def remove_domain_format_capitalize_and_add_emoji(link):
    parsed_url = urlparse(link)
    if parsed_url.netloc:
        formatted_path = parsed_url.path.lstrip('/').replace('-', ' ')
        capitalized_path = formatted_path.title()
        result = f"⭐⭐ {capitalized_path}{parsed_url.params}{parsed_url.query}{parsed_url.fragment} ⭐⭐"
        return result
    else:
        return link

def second_code():
    # Replace 'key' with your actual API key
    api_key = '12286gxnvnjoj0jd12f8t'

    input_file = 'output.txt'
    output_file = 'uploads.txt'

    with open(input_file, 'r') as file:
        urls = file.readlines()

    resulting_file_urls = []
    for url in urls:
        url = url.strip()  # Remove any leading/trailing whitespace or newline characters
        resulting_file_url = upload_file_url(api_key, url)
        if resulting_file_url:
            resulting_file_urls.append(resulting_file_url)

    if resulting_file_urls:
        with open(output_file, 'w') as file:
            file.write('\n'.join(resulting_file_urls))
        print('File URLs written to', output_file)
    else:
        print('No file URLs to write.')

    print("Running second code...")
    # Simulating some work
    for i in range(5):
        print("Second code: Working...")
    
    print("Second code finished!")

def upload_file_url(api_key, file_url):
    upload_url = f'https://pdisk.pro/api/upload/url?key={api_key}&url={file_url}&fld_id=0'
    response = requests.get(upload_url)
    upload_result = response.json()

    if 'result' in upload_result and 'file_code' in upload_result['result']:
        file_code = upload_result['result']['file_code']
        file_url = f'https://pdisk.pro/{file_code}'
        return file_url

    print('Failed to upload file URL:', upload_result)
    return None

# Create a thread for the first code
thread1 = threading.Thread(target=first_code)

# Start the thread for the first code
thread1.start()

# Wait for the first code to finish
thread1.join()

# Run the second code
second_code()
