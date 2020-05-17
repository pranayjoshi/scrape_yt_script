from pytube import YouTube
from pytube import Playlist
def percent(tem, total):
        perc = (float(tem) / float(total)) * float(100)
        return perc

def progress_meter(chunk, file_handle, bytes_remaining):

    global file_size
    p = 0
    progress = p
    p = percent(file_size-bytes_remaining, file_size)
    print('%.1f%s \r' % (p,"%"))
def best_q_single_vid(path):
    yt_link = input("Enter the youtube video link:")
    print(f"Your video will be saved to: {path}")
    print ("Accessing YouTube URL...")
    try:
        yt = YouTube(yt_link, on_progress_callback=progress_meter)
    except:
        print("ERROR. Check your:\n  -connection\n  -url is a YouTube url\n\nTry again.")
        redo = best_q_single_vid(path)
    title = yt.title
    print (f"Fetching: {title}...")
    vid = yt.streams.filter(progressive = True, file_extension = "mp4").first()
    global file_size
    file_size = vid.filesize
    print('FileSize : ' + str(round(vid.filesize/(1024*1024))) + 'MB')
    vid.download(path)
    print('Task Completed!')  
    
    rep_process()

def best_q_playlist(path):
    link = input("Enter the youtube video link:")
    try:
        pl = Playlist(link)
    except:
        print("ERROR. Check your:\n  -connection\n  -url is a YouTube url\n\nTry again.")
        redo = best_q_single_vid(path)
    pl.download_all(path)
    print("task completed")
    rep_process()
def rep_process():
    file_size = 0
    a = input("Do you want to download another video or playlist.")
    if a== "Yes" or a=="yes" or a=='YES':
        a = input("press 1 to download a single vid\nPress 2 to download a playlist\n")
        if a== "1":
            print("Ready to download another video.\n\n")
            best_q_single_vid(path)
        elif a=="2":
            print("Ready to download another video.\n\n")
            best_q_playlist(path)
        else:
            print("process end")
    else:
        print("Thank you!")
if __name__ == "__main__":
    file_size = 0
    path = "C:/Users\prana\OneDrive\Desktop\python_main_files"
    vid_play = input("press 1 to download a single vid\nPress 2 to download a playlist\n")
    if vid_play == "1":
        best_q_single_vid(path)
    elif vid_play == "2":
        best_q_playlist(path)
    else:
        print("process end")
