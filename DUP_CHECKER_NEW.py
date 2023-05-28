import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def compare_and_update_files():
    # Read the contents of dup_checked.txt
    with open('dup_checked.txt', 'r') as dup_checked_file:
        dup_checked_links = set(line.strip() for line in dup_checked_file)

    # Read the contents of output.txt
    with open('all_links.txt', 'r') as output_file:
        output_links = set(line.strip() for line in output_file)

    # Remove duplicate links from dup_checked_links
    initial_count = len(dup_checked_links)
    dup_checked_links -= output_links
    removed_count = initial_count - len(dup_checked_links)

    # Append unique links to output.txt
    added_count = 0
    with open('all_links.txt', 'a') as output_file:
        for link in dup_checked_links:
            output_file.write(link + '\n')
            added_count += 1

    # Append unique links to dup_checked.txt
    with open('dup_checked.txt', 'a') as dup_checked_file:
        for link in dup_checked_links:
            dup_checked_file.write(link + '\n')

    # Logging
    logging.info(f'Removed {removed_count} duplicate link(s) from dup_checked.txt')
    logging.info(f'Added {added_count} unique link(s) to both all_links.txt and dup_checked.txt')

# Call the function to compare and update the files
compare_and_update_files()
