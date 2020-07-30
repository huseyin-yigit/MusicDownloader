from tkinter import *
from youTube_downloader import download_video
from popup import popup_message
from music_converter import convert_mp4_to_mp3
from music_player import play_music



root = Tk()

def call_downloder(link):
    global title 
    title = download_video(link)
    if(title == "No video Found"):
        popup_message("Something Went Wrong, Please check your inputs","red")
         
    else:
        popup_message(title+" was downloaded successfully","green")
       
        
def call_convert(new_file_name):
    global title 
    isConverted = convert_mp4_to_mp3(title,new_file_name)
    if(isConverted):
         popup_message(title+" was converted successfully to "+ new_file_name,"green")
    
    else:
         popup_message("Something Went Wrong, Please Contact developer","red")
       

root.geometry("500x500")
root.title("YouTube Downloader")  
Title=Label(root,text="Welcome to YouTube Downloader",fg='red',font=("Arial Bold",30))
Title.pack()

video_link_message = Label(root,text="Enter YouTube video Link",font=("Arial Bold",15))
video_link_message.pack()
videoLinkInput = Entry(root,bd=5)
videoLinkInput.pack()

download = Button(root,text="Download",fg='blue', bg='black',height = 2, width = 10,command=lambda:call_downloder(videoLinkInput.get()))
download.pack()
video_convert_message = Label(root,text="What you want to call the file",font=("Arial Bold",15))
video_convert_message.pack()
video_convert_entery = Entry(root,bd=5)
video_convert_entery.pack()

convert = Button(root,text="Convert",fg='blue', bg='black',height = 2, width = 10,command=lambda:call_convert(video_convert_entery.get()))
convert.pack()

play = Button(root,text="Play",fg='blue', bg='black',height = 2, width = 10,command=lambda:play_music(video_convert_entery.get()))
play.pack(side = BOTTOM)

root.mainloop()