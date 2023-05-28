import tkinter as tk
from tkinter import filedialog, messagebox

def remove_duplicate_links():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    
    if not file_path:
        return
    
    deleted_links = []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        unique_links = list(set(lines))
        deleted_links = [link for link in lines if link not in unique_links]
        
    with open(file_path, 'w') as file:
        file.writelines(unique_links)
    
    log_box.delete(1.0, tk.END)  # Clear previous log
    log_box.insert(tk.END, f'Deleted {len(deleted_links)} duplicate link(s):\n')
    
    for link in deleted_links:
        line_number = lines.index(link) + 1
        log_box.insert(tk.END, f'- Line {line_number}: {link}')
    
    log_box.insert(tk.END, '\nDuplicate links have been removed.')
    log_box.see(tk.END)  # Scroll to the end of the log
    
    messagebox.showinfo('Duplicate Link Remover', 'Duplicate links have been removed.')

# Create the main window
window = tk.Tk()
window.title('Duplicate Link Remover')

# Create a button to open the file dialog
open_button = tk.Button(window, text='Open File', command=remove_duplicate_links)
open_button.pack(pady=10)

# Create a log box to display the results
log_box = tk.Text(window, height=40, width=80)
log_box.pack()

# Start the Tkinter event loop
window.mainloop()
