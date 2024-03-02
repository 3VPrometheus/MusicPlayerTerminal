import dLoaderLibsTerminal
import os
import prereqs
from shutil import copy

# This app is designed to be run in a Termux environment, so the following code is designed to work in that environment


class MusicDownloader(dLoaderLibsTerminal):

    def __init__(self):
        self.download_dir = "/data/data/com.termux/files/home/Music"
        self.music_dir = "/storage/emulated/0/Music"
    
    def download_music(self):
        searchTerm = input("Enter the name of the song you want to download: \n")
        numResults = int(input("Enter the number of results you want to see: \n"))
        
        video_link = self.SearchYoutube(searchTerm, numResults)
        file_name = input("Enter what to name the audio file: \n")
        
        self.downloadYouTubeAudio(video_link, self.download_dir, file_name)
        
        # Copy the downloaded file to the music directory
        copy(f"{self.download_dir}/{file_name}.mp4", f"{self.music_dir}/{file_name}.mp4")