from shutil import copy
from youtubesearchpython import VideosSearch
from pytube import YouTube
import sys
from argparse import ArgumentParser

# This app is designed to be run in a Termux environment, so the following code is designed to work in that environment

class Downloader:
    '''
    This class is designed to search for and download music from YouTube
    '''
    @staticmethod
    def SearchYoutube(searchTerm : str, numResults : int) -> str:
        '''
        This method searches for a song on YouTube and returns the link to the video
        '''
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
        '''
        This method downloads the audio from a YouTube video
        '''
        YouTube(url=videoLink).streams.filter(only_audio=True).first().download(output_path=download_dir, filename=f"{file_name}.mp3")

class MusicDownloader(Downloader):

    def __init__(self):
        
        self.music_dir = "/storage/emulated/0/Music"

        parser = ArgumentParser(prog="MusicDownloader", description="Termux command line tool to download music from YouTube")
        parser.add_argument("--searchterm", type=str, help="The search term given to the YouTube search")
        parser.add_argument("--numresults", type=int, help="The number of results to return from the YouTube search, default is 10", default=10)
        parser.add_argument("--outfile", type=str, help="The name of the file to save the audio as. If not given, the file will be saved as [searchterm].mp3")
        args = parser.parse_args()
        
        if not args.searchterm:
            sys.exit("Error: --searchterm must be entered.")
        else:
            self.searchTerm = args.searchterm
            self.numResults = args.numresults
        
        self.outputname = None
        if args.outfile:
            self.outputname = args.outfile
    
    def download_music(self):
        video_link = self.SearchYoutube(self.searchTerm, self.numResults)
        filename = self.outputname or self.searchTerm
        
        self.downloadYouTubeAudio(video_link, self.music_dir, filename)

if __name__ == "__main__":
    music_downloader = MusicDownloader()
    music_downloader.download_music()
