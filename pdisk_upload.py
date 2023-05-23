import requests

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
