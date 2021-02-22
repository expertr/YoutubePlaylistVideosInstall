import pytube
import os

os.system("color a")

print("""


 __   __        _        _         ___ _           _ _    _ __   ___    _            ___         _        _ _ 
 \ \ / /__ _  _| |_ _  _| |__  ___| _ \ |__ _ _  _| (_)__| |\ \ / (_)__| |___ ___ __|_ _|_ _  __| |_ __ _| | |
  \ V / _ \ || |  _| || | '_ \/ -_)  _/ / _` | || | | (_-<  _\ V /| / _` / -_) _ (_-<| || ' \(_-<  _/ _` | | |
   |_|\___/\_,_|\__|\_,_|_.__/\___|_| |_\__,_|\_, |_|_/__/\__|\_/ |_\__,_\___\___/__/___|_||_/__/\__\__,_|_|_|
                                              |__/                                                            

             
""")

playlistID = input("[+] Insert playlist ID: ")

path = os.path.abspath(os.getcwd()) + r"\\"

counter = 0

def counterAdd():
    global counter
    counter += 1
    return counter

try:
    playlist = pytube.Playlist(f"https://www.youtube.com/playlist?list={playlistID}")
    print(f"[+] Starting {len(playlist)} install videos...")
    os.mkdir(path + playlist.title)
    for videoURL in playlist:
        if counter == len(playlist):
            print("[+] Finished !")
        else:
            video = pytube.YouTube(videoURL)
            print(f"[+] #{counterAdd()} - '{video.title}' Downloading")
            video.streams.filter(file_extension='mp4').first().download(output_path=path + playlist.title)
except: 
    os.system("color c")
    print("[-] Error !!")
