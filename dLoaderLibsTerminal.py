from youtubesearchpython import VideosSearch
from pytube import YouTube

def SearchYoutube(searchTerm : str, numResults : int) -> str:
    '''Returns a dictionary - videoIDs - in the format {"videoID" - "videoTitle"}
    where video id is the id later used in the youtube.com/watch?v=... link
    
    Also returns a list of corresponding video durations, used to display how long each video is
    when displaying search results
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

def downloadYouTubeAudio(videoLink : str, download_dir : str, file_name : str) -> None:

    YouTube(url=videoLink).streams.filter(only_audio=True).first().download(output_path=download_dir, filename=f"{file_name}.mp4")