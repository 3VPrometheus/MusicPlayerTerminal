import dLoaderLibsTerminal
import os
import prereqs

# This app is designed to be run in a Termux environment, so the following code is designed to work in that environment


class MusicDownloader(dLoaderLibsTerminal, prereqs):

    def __init__(self):
        # Currently /data/data/com.termux/files/home/Music
        # This is the default download directory for the app
        # Files should also be copied to /storage/shared/Music/ for the files to be accessible to other apps
        self.download_dir = "/data/data/com.termux/files/home/Music"
        self.music_dir = "/storage/emulated/0/Music"
        
        MusicDownloader.get_prereqs()