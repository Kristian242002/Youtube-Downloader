from difflib import Match
from turtle import Screen, bgcolor
from pytube import YouTube
import tkinter as tk
import os

#download mp3 function
def downloadMp3():
    url = campoUrl.get()
    if url == "":
        window.title("Errore inserire un link valido!")
    else:
            window.title("Sto Scaricando......")
            audio = YouTube(url).streams.filter(only_audio=True).first()
            out_file = audio.download("Video")
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            window.title("Hai completato il Download, Se vuoi puoi scaricare un altro file..")

#download mp4/video function
def downloadMp4():
    url = campoUrl.get()
    if url == "":
        window.title("Errore inserire un link valido!")
    else:
            window.title("Sto Scaricando......")
            video = YouTube(url).streams.get_highest_resolution()
            video.download("Video")
            window.title("Hai completato il Download, Se vuoi puoi scaricare un altro file..")


#MAIN()
#window settings
window = tk.Tk()
window.geometry("350x300")
window.resizable(0, 0)
window.title("Youtube Downloader by Kristo 0.0.0")
window.configure(bg="#F2F2F2")
window.grid_columnconfigure(0)
window.wm_iconbitmap("Img\icoyoutube.ico")
#url label + campo di inserimento
urlLbl = tk.Label(window,text="INSERISCI URL DEL VIDEO",font=("Arial",14)) 
urlLbl.grid(row=1,column=1,pady=5,padx=5)

campoUrl = tk.Entry(window,width=55)
campoUrl.grid(row=2,column=1,pady=5,padx=5)
#bottone download mp3 e mp4
btnMp3=tk.Button(text="Download mp3",command=downloadMp3)
btnMp3.grid(row=3,column=1,pady=5,padx=5)
btnMp4=tk.Button(text="Download mp4",command=downloadMp4)
btnMp4.grid(row=4,column=1,pady=5,padx=5)

window.mainloop()