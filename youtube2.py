from pytube import Playlist, YouTube
from pytube import Search
from pytube import Channel
from pytube import YouTube
YouTube('https://www.youtube.com/watch?v=p1-sSgd2V1I').streams.first().download()
#yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
#yt.streams .filter(progressive=True, file_extension='mp4') .order_by('resolution').desc().first().download()


yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
print(yt.title)

yt = YouTube(
    'http://youtube.com/watch?v=2lAe1cqCOXo',
    on_progress_callback=progress_func,
    on_complete_callback=complete_func,
    proxies=my_proxies,
    use_oauth=False,
    allow_oauth_cache=True
)

for i in yt.streams:
    print(i)

yt.streams.filter(only_audio=True)  # audio-only streams
yt.streams.filter(adaptive=True)
yt.streams.filter(file_extension='mp4')  # mp4

stream = yt.streams.get_by_itag(22)
stream.download()


c = Channel('https://www.youtube.com/c/ProgrammingKnowledge')
print(f'Downloading videos by: {c.channel_name}')
# Downloading videos by: ProgrammingKnowledge
for video in c.videos:
    video.streams.first().download()


s = Search('YouTube Rewind')
len(s.results)


playlist_url = 'https://www.youtube.com/results?search_query=%E7%B2%A4%E8%AF%AD%E9%87%91%E6%9B%B2'
p = Playlist(playlist_url)
for url in p.video_urls:
    try:
        yt = YouTube(url)
    except VideoUnavailable:
        print(f'Video {url} is unavaialable, skipping.')
    else:
        print(f'Downloading video: {url}')
        yt.streams.first().download()
