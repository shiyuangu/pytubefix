from pytubefix import YouTube

#url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
url = 'https://www.youtube.com/watch?v=l3rDobdu1gU'
# to reset oauth cache: https://pytubefix.readthedocs.io/en/latest/user/auth.html#reset-cache
yt = YouTube(url, client='WEB', use_oauth=True)
#yt = YouTube(url, client='WEB')
#print(yt.vid_info)
# ys = yt.streams.get_highest_resolution()
# #ys= yt.streams.filter(file_extension='mp4')[0]
# #ys = yt.streams.get_by_itag(137)
# print(ys)
# output_path = '/Users/sgu/Downloads'
# ys.download(output_path=output_path)

video_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first()
audio_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first()
print('video_stream:',video_stream)
print('audio_stream:',audio_stream)
output_path = '/Users/sgu/Downloads'
video_stream.download(filename='test_video.mp4', output_path=output_path)
audio_stream.download(filename='test_audio.mp4', output_path=output_path)