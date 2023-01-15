import tkinter
import customtkinter
from pytube import YouTube

# Download Function


def downFunc():
    try:
        videolink = link.get()
        video_obj = YouTube(videolink, on_progress_callback=onProgress)
        video = video_obj.streams.get_highest_resolution()
        finishlab.configure(text="")
        video.download()

        finishlab.configure(text="Download Complete!", text_color="green")
        vidTitle.configure(text=video.title, font=('Arial', 20))
    except:
        finishlab.configure(
            text="Error Occurred! Maybe the link is invalid.", text_color="red")


def onProgress(stream, chunk, bytes_remaining):
    print("function works")
    total = stream.filesize
    downBytes = total - bytes_remaining
    downPercent = downBytes/total*100
    percent = str(int(downPercent))
    # Updating the percentage
    progpercent.configure(text=percent+'%', font=('Roboto', 16))
    progpercent.update()
    # Updateing the bar
    progbar.set(float(downPercent)/100)


# System Settings
customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("green")

# GUI frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI elements
title = customtkinter.CTkLabel(
    app, text="Paste  YouTube Link", font=('Poppins', 30))
title.pack(padx=10, pady=10)
# Link ENtry
urlvar = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=urlvar)
link.pack()

# Download Complete
finishlab = customtkinter.CTkLabel(app, text="")
finishlab.pack()
# Video Title
vidTitle = customtkinter.CTkLabel(
    app, text="")
vidTitle.pack()

# Download Percent
progpercent = customtkinter.CTkLabel(app, text="0%")
progpercent.pack()

# Progressbar
progbar = customtkinter.CTkProgressBar(app, width=400)
progbar.set(0)
progbar.pack(padx=10, pady=10)

# Download Button
downloadbtn = customtkinter.CTkButton(
    app, text="Download", command=downFunc, fg_color="#820d38", hover_color="#0d6163")
downloadbtn.pack(pady=20)
app.mainloop()
