from shutil import copy
from youtubesearchpython import VideosSearch
from pytube import YouTube

# This app is designed to be run in a Termux environment, so the following code is designed to work in that environment

class Downloader:
    
    @staticmethod
    def SearchYoutube(searchTerm : str, numResults : int) -> str:

        videos = VideosSearch(searchTerm, numResults).result()

        videoIDs = {}
        video_duration = []
        
        video_link = ""

        for video in videos["result"]:
            if not video['duration'] or len(video['duration'].split(":")) > 2 or int(video['duration'].split(":")[0]) > 10:
                continue
            else:
                videoIDs[video['id']] = video['title']
                video_duration.append(video['duration'])
        
        for i, vidTitle in enumerate(videoIDs.values()):
            print(f"[{i}] --> {vidTitle} || duration: {video_duration[i]}")
        
        selection = int(input("Enter the number of the video you want to download: \n"))
        
        videoID = list(videoIDs.keys())[selection]
        
        video_link = f"https://www.youtube.com/watch?v={videoID}"
        return video_link
    
    @staticmethod
    def downloadYouTubeAudio(videoLink : str, download_dir : str, file_name : str) -> None:

        YouTube(url=videoLink).streams.filter(only_audio=True).first().download(output_path=download_dir, filename=f"{file_name}.mp3")

class MusicDownloader(Downloader):

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
        copy(f"{self.download_dir}/{file_name}.mp3", f"{self.music_dir}/{file_name}.mp3")