# Read the contents of "names.txt"
with open("name.txt", "r") as names_file:
    names = names_file.read().splitlines()

# Read the contents of "upload.txt"
with open("uploads.txt", "r") as upload_file:
    links = upload_file.read().splitlines()

# Merge the names and links
merged_content = []
for i in range(len(names)):
    merged_content.append(f"{i+1}. {names[i]}")
    merged_content.append(links[i])
    merged_content.append("")  # Add an empty string for a line break

# Join the merged content with line breaks
merged_text = "\n".join(merged_content)

# Write the merged content into "upload.txt"
with open("uploads.txt", "w") as output_file:
    output_file.write(merged_text)
