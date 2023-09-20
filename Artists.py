import tkinter as tk
from tkinter import ttk

# Main Window
root = tk.Tk()
root.title("Famous Artists Information")

# Artist Data
artist_data = {
    'Leonardo da Vinci': 'An Italian polymath. Known for works like The Last Supper and Mona Lisa.',
    'Pablo Picasso': 'A Spanish painter. Known for co-founding the Cubist movement.',
    'Vincent van Gogh': 'A Dutch Post-Impressionist painter. Known for works like Starry Night.',
    'Michelangelo': 'An Italian sculptor, painter, and architect. Known for works like David and Sistine Chapel Ceiling.',
    'Claude Monet': 'A French painter. Known for leading the Impressionist movement.'
}

# Label
label = ttk.Label(root, text="Select an Artist:")
label.pack(pady=10)

# Combobox
artist_name = tk.StringVar()
artist_combobox = ttk.Combobox(root, width=40, textvariable=artist_name)
artist_combobox['values'] = list(artist_data.keys())
artist_combobox.pack(pady=10)

# Text Widget
artist_info_display = tk.Text(root, width=50, height=10, wrap=tk.WORD)
artist_info_display.pack(pady=10)

# Function to Update Text widget
def update_info(event):
    artist = artist_name.get()
    info = artist_data.get(artist, 'No information available')
    artist_info_display.delete(1.0, tk.END)
    artist_info_display.insert(tk.INSERT, info)

# Bind Combobox select event
artist_combobox.bind("<<ComboboxSelected>>", update_info)

# Run Tkinter event loop
root.mainloop()
