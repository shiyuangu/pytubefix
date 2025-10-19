import logging
from pytubefix import YouTube
import logging
import logging
logging.basicConfig(format='%(filename)s:%(lineno)d:%(funcName)s:%(message)s') # this creates a default handler (which is a /StreamHandler/ to stderr) for the root logger only if the root logger has no handlers attached otherwise does nothing. only for local-dev; aws will attach root_logger.handlers [<LambdaLoggerHandler (NOTSET)>] and hence the formatter will be overwritten since formatters are attached to handler.
logger = logging.getLogger("pytubefix").setLevel(logging.INFO)
#logger.setLevel(logging.INFO)  # cannot set level in basicConfig which would be overwritten by aws.
#url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
#url = 'https://www.youtube.com/watch?v=l3rDobdu1gU'
#url = 'https://www.youtube.com/watch?v=020g-0hhCAU'
#url = 'https://www.youtube.com/watch?v=U5Inxa3jK0Y'
#url = 'https://www.youtube.com/watch?v=u6GatvmKd3s'
#url = 'https://www.youtube.com/watch?v=DHMxk2KvAyI'
#url = 'https://www.youtube.com/watch?v=GE3uj-TB-oo'
#fname= "playlist_baby_tiger_long"
url = 'https://www.youtube.com/watch?v=dXa-ZxpXf6s'
fname= "playlist_baby_tiger_chinese"
# to reset oauth cache: https://pytubefix.readthedocs.io/en/latest/user/auth.html#reset-cache
yt = YouTube(url,  use_oauth=True) 
#yt = YouTube(url, client='WEB') # look like client='WEB' has no effect for use_oauth=True which always use client='TV' see the Youtube.ctor code
#print(yt.vid_info)
# ys = yt.streams.get_highest_resolution()
# #ys= yt.streams.filter(file_extension='mp4')[0]
# #ys = yt.streams.get_by_itag(137)
# print(ys)
# output_path = '/Users/sgu/Downloads'
# ys.download(output_path=output_path)
print('title:',yt.title)
video_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first()
audio_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first()
print('video_stream:',video_stream)
print('audio_stream:',audio_stream)
output_path = '/Users/sgu/Downloads'
video_stream.download(filename=f'{fname}_video.mp4', output_path=output_path)
audio_stream.download(filename=f'{fname}_audio.mp4', output_path=output_path)
# Combine video and audio using ffmpeg
import subprocess
video_file = f'{output_path}/{fname}_video.mp4'
audio_file = f'{output_path}/{fname}_audio.mp4'
output_file = f'{output_path}/{fname}.mp4'
cmd = [
	'ffmpeg',
	'-i', video_file,
	'-i', audio_file,
	'-c', 'copy',
	output_file
]
print('Running ffmpeg to combine video and audio...')
result = subprocess.run(cmd, capture_output=True, text=True)
if result.returncode == 0:
	print(f'Successfully created {output_file}')
else:
	print('ffmpeg failed:', result.stderr)

