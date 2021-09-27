from pytube import YouTube
import os

def get_audio_id(url):
    try:
        id = url[-10:]
        return id
    except:
        pass

def get_vid(id):
    try:
        video = os.listdir(f"downloads/{id}")[0]
        return video
    except:
        pass

def download_song(url, id):
    if not id in os.listdir("downloads/"):
        try:
            url = str(url).strip()
            song = YouTube(url)
            song.streams.filter(only_audio=True, file_extension="mp4").first().download(f'downloads/{id}')
        except:
            pass
