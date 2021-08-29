from moviepy import editor

video = editor.VideoFileClip('camera movement.mp4')
video.audio.write_audiofile('camera movement.mp3')