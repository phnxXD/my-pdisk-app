from urllib.parse import urlparse

def remove_domain_format_capitalize_and_add_emoji(link):
    parsed_url = urlparse(link)
    if parsed_url.netloc:
        formatted_path = parsed_url.path.lstrip('/').replace('-', ' ')
        capitalized_path = formatted_path.title()
        result = f"⭐⭐ {capitalized_path}{parsed_url.params}{parsed_url.query}{parsed_url.fragment} ⭐⭐"
        return result
    else:
        return link

# Read links from file
with open('links.txt', 'r') as file:
    links = file.read().splitlines()

# Process links
output = []
for link in links:
    result_with_emojis = remove_domain_format_capitalize_and_add_emoji(link)
    output.append(result_with_emojis)

# Save output to file
with open('name.txt', 'w') as file:
    file.write('\n'.join(output))
