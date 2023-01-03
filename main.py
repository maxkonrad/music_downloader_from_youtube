import os, time
from pytube import YouTube

print("This Python 3 program downloads the music files in the dedicated directory")
file_dir = input("Please enter file directory leave blank for it to be default (video_links.txt)") or './video_links.txt'
out_folder = 'out_folder'

if not os.path.exists(out_folder):
    os.makedirs(out_folder)

count = 0

print("Reading Text File")

with open(file_dir) as fp:
    while True:
        count += 1
        time.sleep(3)
        line = fp.readline()
        if not line:
            break
        line = YouTube(fp.readline())
        print("Downloading MP3 at line {}: {}".format(count, line.title))
        try:
            video = line.streams.filter(only_audio=True).first()
            out_file = video.download(output_path = out_folder)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

            print(line.title + " has been successfully downloaded.")
            
        except Exception as exception:
            print("Invalid link at line: {}".format(count))
            print("Error: {}".format(exception))
            continue
        
