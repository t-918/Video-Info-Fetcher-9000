import pytube
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Function to convert seconds to "hh:mm:ss" format (to make this readable for dummies)
def format_duration(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

# Function to format views count with commas (making big numbers easier to read)
def format_views(views):
    return f"{views:,}"

# Function to fetch video information
def fetch_video_info():
    video_url = video_link_entry.get()
    try:
        yt = pytube.YouTube(video_url)
        
        # Close the main window
        root.destroy()

        # Create a new info window
        info_window = tk.Tk()
        info_window.title("Video Information")
        info_window.geometry("691x259")
        info_window.configure(bg="black")

        # Make the info window unresizable (can't stretch this, folks)
        info_window.resizable(False, False)

        # Create a Text widget for displaying information (the text box, you know)
        text_widget = tk.Text(info_window, font=("Arial Rounded MT Bold", 12), wrap=tk.WORD, background="black", foreground="white", state=tk.DISABLED)
        text_widget.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Insert video information into the Text widget
        text_widget.configure(state=tk.NORMAL)
        text_widget.insert(tk.END, f"Title: {yt.title}\n\n")
        text_widget.insert(tk.END, f"Video ID: {yt.video_id}\n\n")
        text_widget.insert(tk.END, f"Author: {yt.author}\n\n")
        text_widget.insert(tk.END, f"Views: {format_views(yt.views)}\n\n")  # Format the views count
        text_widget.insert(tk.END, f"Duration: {format_duration(yt.length)}\n\n")  # Format the duration
        text_widget.insert(tk.END, f"Description:\n{yt.description}\n\n")
        text_widget.insert(tk.END, f"Publish Date: {yt.publish_date}\n\n")
        text_widget.configure(state=tk.DISABLED)

        info_window.mainloop()
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title("YouTube Video Info")
    
    # Set the final size directly
    root.geometry("691x259")
    
    # Background color changed to black
    root.configure(bg="black")

    # Make the main window unresizable (don't stretch my limits, please)
    root.resizable(False, False)

    label = ttk.Label(root, text="Enter YouTube Video Link:", font=("Arial Rounded MT Bold", 14), background="black", foreground="white")
    label.pack(pady=12)

    video_link_entry = ttk.Entry(root, font=("Arial Rounded MT Bold", 12))
    video_link_entry.pack(padx=24, pady=6, fill=tk.X)

    fetch_button = ttk.Button(root, text="Fetch Video Info", command=fetch_video_info, style="TButton")
    fetch_button.pack(pady=12)

    style = ttk.Style()
    style.configure("TButton", font=("Arial Rounded MT Bold", 12))

    root.mainloop()
