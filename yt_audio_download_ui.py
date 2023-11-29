import tkinter
import customtkinter
from pytube import YouTube

# Functions
def start_download():
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link, on_progress_callback=download_progress)
        audio = yt_object.streams.get_audio_only()
        title.configure(text=yt_object.title, text_color="white")
        finish_label.configure(text="")
        audio.download()
        finish_label.configure(text="Download Complete!")
    except:
        finish_label.configure(text="YouTube Link Invalid", text_color="red")
    
def download_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    progress_percentage.configure(text=per + '%')
    progress_percentage.update()

    # Update Progress Bar
    progress_bar.set(float(percentage_of_completion) / 100)

def close_app():
    quit()

# System Settings (UI)
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

# App Frame
app = customtkinter.CTk()
app.geometry("480x300")
app.title("Youtube Audio Downloader")

# UI Elements
title = customtkinter.CTkLabel(app, text="Insert YouTube Link")
title.pack(padx=10, pady=10)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading Text
finish_label = customtkinter.CTkLabel(app, text="")
finish_label.pack()

# Progress Bar
progress_percentage = customtkinter.CTkLabel(app, text="0%")
progress_percentage.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=start_download)
download.pack(pady=15)

# Close App Button
close_button = customtkinter.CTkButton(app, text="Quit App", command=close_app)
close_button.pack(pady=5)

# Run App
app.mainloop()
