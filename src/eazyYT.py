from customtkinter import *
import yt_dlp

ytb_link = "https://www.youtube.com/watch?v="
ydl_opts = {}

def downloader_yt():
    
    file = open("config.txt","r")
    for i in file:
        if i.startswith("format= "):
            i=i.rstrip()
            format = i.strip("format=")
            format = format.strip(" ")
        elif i.startswith("playlist= "):
            i=i.rstrip()
            i= i.strip("playlist= ")
            if i == "True":
                playlist = True
            elif i == "False":
                playlist = False

        elif i.startswith("link= "):
            url = str(i.strip("link= "))
    print(format, type(playlist), url)
    file.close()
    winds = CTkToplevel(app)
    winds.geometry("500x100")
    winds.title("Download complete!")
    label = CTkLabel(winds, text="check the mp3 or mp4 folders in the main folder") 
    label.pack(padx=20, pady=20)
    winds.transient(app) 
    winds.focus_set()
    winds.resizable(False,False)
    if format == "mp3":
        ydl_opts = {
            'noplaylist': playlist,
            'paths': {'home': "mp3"},
            'format': 'bestaudio',
            'write_thumbnail': True,
            'embed_thumbnail': True,
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio', 
                'preferredcodec': 'mp3',      
                'preferredquality': '192',     
            }],
            'ignoreerrors': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    elif format == "mp4":
        ydl_opts = {
            'noplaylist': playlist,
            'paths': {'home': "mp4"},
            'format': "bestvideo[ext=mp4]+bestaudio[ext=m4a]",
            'write_thumbnail': True,
            'embed_thumbnail': True,
            'outtmpl': '%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    text = open("config.txt","w")
    text.write("format= mp4\nplaylist= False\n")
    text.close()
    winds.destroy()
    
def error_vid():
    wind = CTkToplevel(app)
    wind.geometry("300x100")
    wind.title("Error")
    wind.resizable(False,False)
    label = CTkLabel(wind, text="Link invalido!") 
    label.pack(padx=20, pady=20)
    text = open("config.txt","w")
    text.write("format= mp4\nplaylist= False\n")
    text.close()
    return

def change_playlist_false(window):
    window.destroy()
    lista = []
    file = open("config.txt","r")
    for i in file:
        i=i.rstrip()
        lista.append(i)
    file.close()
    lista[1] = "playlist= True"
    text = str(lista[0]+"\n"+lista[1]+"\n"+lista[2])
    file = open("config.txt","w")
    file.write(text)
    file.close()
    downloader_yt()

def change_playlist_true(window):
    window.destroy()
    downloader_yt()

def set_format(type):
    file = open("config.txt","w")
    file.write("format= " + type + "\nplaylist= False\n")
    file.close()
    
def playlist_window(link):
    window = CTkToplevel(app)
    window.geometry("600x150")
    app.resizable(False,False)
    window.title("Playlist")
    label = CTkLabel(window, text="Do you want to download the full playlist or just the video from the link?",font=("arial",15)) 
    label.pack(padx=20, pady=20)
    button =  CTkButton(window, text="Full playlist ",command=lambda: change_playlist_true(window)).place(x=125,y=80)
    button2 = CTkButton(window, text="Just the video",command=lambda: change_playlist_false(window)).place(x=325+13,y=80)

def click():
    usr_link = entry.get()
    file = open("config.txt","a")
    file.write(f"link= {usr_link}")
    file.close()
    if usr_link[:len(ytb_link)] == ytb_link:
        entry.delete(0,END)
        temp = usr_link.split("&list=")
        if len(temp) == 2:
            playlist_window(usr_link)
        else:
            downloader_yt()
    elif usr_link == "":
        return

    else:
        error_vid()
    
text = open("config.txt","w")
text.write("format= mp4\nplaylist= False\n")
text.close()

set_appearance_mode("dark")
app = CTk() 
app.geometry("600x300")
app.resizable(False,False)
app.title("EazyYT")

texto = CTkLabel(app,text="Enter the youtube link:",font=("arial",20)).pack(padx=20,pady=10)
entry = CTkEntry(master=app,width=500,placeholder_text= "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
entry.pack(pady=10)

texto2 = CTkLabel(app,text="\nIf the program is frozen, DO NOT close it! It is just downloading the files :)\nWhen the program unfreezes, check the 'mp4' or 'mp3' folders to see your downloads!\n\nSelect the format to be downloaded:").pack(pady=5)

opcao = CTkOptionMenu(app,values=["mp4","mp3"],command=set_format)
opcao.set("mp4")
opcao.pack(pady=10)

button = CTkButton(app, text="Download!",command=click).pack()

app.mainloop()